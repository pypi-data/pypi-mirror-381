import functools
from collections.abc import Callable
import inspect
import json
from typing import Optional, Any
import builtins

from oprc_py.oprc_py import (
    InvocationRequest,
    InvocationResponse,
    InvocationResponseCode,
    ObjectInvocationRequest,
)
from pydantic import BaseModel

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from oaas_sdk2_py.engine import BaseObject
    from oaas_sdk2_py.simplified.accessors import AccessorSpec  


class FuncMeta:
    def __init__(
        self,
        func,
        invoke_handler: Callable,
        signature: inspect.Signature,
        name,
        stateless=False,
        serve_with_agent=False,
        is_async=False,
    ):
        self.func = func
        self.invoke_handler = invoke_handler
        self.signature = signature
        self.stateless = stateless
        self.name = name
        self.serve_with_agent = serve_with_agent
        self.is_async = is_async
        self.__name__ = func.__name__
        self.__qualname__ = func.__qualname__
        self.__doc__ = func.__doc__

    def __get__(self, obj, objtype=None):
        """
        Descriptor protocol method that handles method binding when accessed through an instance.

        Args:
            obj: The instance the method is being accessed through (or None if accessed through the class)
            objtype: The class the method is being accessed through

        Returns:
            A bound method if accessed through an instance, or self if accessed through the class
        """
        if obj is None:
            # Class access - return the descriptor itself
            return self

        if inspect.iscoroutinefunction(self.func):
        # Instance access - return a bound method
            async def bound_method(*args, **kwargs):
                return await self.func(obj, *args, **kwargs)
        else:
            def bound_method(*args, **kwargs):
                return self.func(obj, *args, **kwargs)
            
        # Copy over metadata from the original function to make the bound method look authentic
        bound_method.__name__ = self.__name__
        bound_method.__qualname__ = self.__qualname__
        bound_method.__doc__ = self.__doc__
        bound_method._meta = self
        bound_method._owner = obj

        return bound_method

    def __call__(self, obj_self, *args, **kwargs):
        """
        Make FuncMeta callable, allowing direct invocation when accessed through a class.

        Args:
            obj_self: The object instance (self from the original method)
            *args: Positional arguments
            **kwargs: Keyword arguments

        Returns:
            The result of the function call
        """
        return self.func(obj_self, *args, **kwargs)

    def __str__(self):
        return f"{{name={self.name}, stateless={self.stateless}, serve_with_agent={self.serve_with_agent}}}"

class StateMeta:
    setter: Callable
    getter: Callable

    def __init__(self, index: int, name: Optional[str] = None):
        self.index = index
        self.name = name


def parse_resp(resp, return_type_hint: Optional[type] = None) -> InvocationResponse:
    """
    Enhanced response parser that supports all types using unified serialization.
    
    Args:
        resp: The response value to serialize
        return_type_hint: Optional type hint for better serialization
        
    Returns:
        InvocationResponse with serialized payload
    """
    if resp is None:
        return InvocationResponse(status=int(InvocationResponseCode.Okay))
    elif isinstance(resp, InvocationResponse):
        return resp
    
    # Fast-path for common simple types to avoid unnecessary JSON quoting
    # - If the function declares it returns str, send UTF-8 bytes directly (no JSON quotes)
    # - If the function returns bytes, pass through as-is
    try:
        if return_type_hint is str and isinstance(resp, str):
            return InvocationResponse(status=int(InvocationResponseCode.Okay), payload=resp.encode())
        if return_type_hint is bytes and isinstance(resp, (bytes, bytearray, memoryview)):
            payload = bytes(resp)
            return InvocationResponse(status=int(InvocationResponseCode.Okay), payload=payload)
    except Exception:
        # Fallback to unified serializer path below on any unexpected issue
        pass
    
    # Use unified serialization system for comprehensive type support
    try:
        # Lazy import to avoid circular imports
        from oaas_sdk2_py.simplified.serialization import UnifiedSerializer
        serializer = UnifiedSerializer()
        payload = serializer.serialize(resp, return_type_hint)
        return InvocationResponse(status=int(InvocationResponseCode.Okay), payload=payload)
    except Exception as e:
        # Create error response with detailed information
        error_details = {
            'error_type': type(e).__name__,
            'response_type': type(resp).__name__,
            'return_type_hint': return_type_hint.__name__ if return_type_hint else None,
            'error_message': str(e)
        }
        
        return InvocationResponse(
            status=int(InvocationResponseCode.AppError),
            payload=json.dumps(error_details).encode()
        )


class ClsMeta:
    func_dict: dict[str, FuncMeta]
    state_dict: dict[int, StateMeta]
    accessor_dict: dict[str, "AccessorSpec"]

    def __init__(
        self, name: Optional[str], pkg: str = "default", update: Callable = None
    ):
        self.name = name
        self.pkg = pkg
        self.cls_id = f"{pkg}.{name}"
        self.update = update
        self.func_dict = {}
        self.state_dict = {}
        self.accessor_dict = {}

    def __call__(self, cls):
        """
        Make the ClsMeta instance callable to work as a class decorator.

        Args:
            cls: The class being decorated

        Returns:
            The decorated class
        """
        if self.name is None or self.name == "":
            self.name = cls.__name__
        self.cls = cls
        # Inject the ClsMeta instance into the decorated class
        setattr(cls, "__cls_meta__", self)
        if self.update is not None:
            self.update(self)
        return cls

    def func(self, name="", stateless=False, strict=False, serve_with_agent=False):
        """
        Decorator for registering class methods as invokable functions in OaaS platform.

        Args:
            name: Optional function name override. Defaults to the method's original name.
            stateless: Whether the function doesn't modify object state.
            strict: Whether to use strict validation when deserializing models.

        Returns:
            A FuncMeta instance that wraps the original method and is callable
        """

        def decorator(function):
            """
            Inner decorator that wraps the class method.

            Args:
                function: The method to wrap

            Returns:
                FuncMeta instance that wraps the original method
            """
            fn_name = name if len(name) != 0 else function.__name__
            sig = inspect.signature(function)
            
            if inspect.iscoroutinefunction(function):
                
                @functools.wraps(function)
                async def async_wrapper(obj_self: "BaseObject", *args, **kwargs):
                    """
                    Wrapper function that handles remote/local method invocation.

                    Args:
                        obj_self: The object instance
                        *args: Positional arguments
                        **kwargs: Keyword arguments

                    Returns:
                        The result of the function call or a response object
                    """
                    if obj_self.remote:
                        if stateless:
                            req = self._extract_request(
                                obj_self, fn_name, args, kwargs, stateless, sig
                            )
                            resp = await obj_self.session.fn_rpc_async(req)
                        else:
                            req = self._extract_request(
                                obj_self, fn_name, args, kwargs, stateless, sig
                            )
                            resp = await obj_self.session.obj_rpc_async(req)
                        # Raise on non-OK status
                        if resp.status != int(InvocationResponseCode.Okay):
                            try:
                                details = json.loads(resp.payload.decode()) if resp.payload else {}
                            except Exception:
                                details = {'error_message': resp.payload.decode(errors='ignore')}
                            err_type = details.get('error_type') or 'Exception'
                            err_msg = details.get('error_message') or details.get('last_error') or str(details)
                            # Resolve to SDK-specific exception when possible
                            exc_cls = None
                            try:
                                from oaas_sdk2_py.simplified import errors as _sdk_errors  # type: ignore
                                exc_cls = getattr(_sdk_errors, err_type, None)
                            except Exception:
                                exc_cls = None
                            if exc_cls is None:
                                exc_cls = getattr(builtins, err_type, Exception)
                            raise exc_cls(err_msg)
                        # Map payload to annotated return type using UnifiedSerializer
                        ret_anno = sig.return_annotation
                        if ret_anno is inspect._empty or ret_anno is None:
                            # Best-effort decode for unannotated returns: provide attribute-style access
                            if not resp.payload:
                                return None
                            try:
                                from oaas_sdk2_py.simplified.serialization import UnifiedSerializer
                                _ser = UnifiedSerializer()
                                val = _ser.deserialize(resp.payload, Any)
                            except Exception:
                                try:
                                    val = json.loads(resp.payload.decode())
                                except Exception:
                                    return None
                            try:
                                from types import SimpleNamespace
                                def _to_attr(x):
                                    if isinstance(x, dict):
                                        return SimpleNamespace(**{k: _to_attr(v) for k, v in x.items()})
                                    if isinstance(x, list):
                                        return [ _to_attr(i) for i in x ]
                                    return x
                                return _to_attr(val)
                            except Exception:
                                return val
                        try:
                            if inspect.isclass(ret_anno) and issubclass(ret_anno, BaseModel):
                                return ret_anno.model_validate_json(resp.payload, strict=strict)
                        except Exception:
                            pass
                        if ret_anno is bytes:
                            return resp.payload
                        if ret_anno is str:
                            return resp.payload.decode()
                        from oaas_sdk2_py.simplified.serialization import UnifiedSerializer
                        _ser = UnifiedSerializer()
                        return _ser.deserialize(resp.payload, ret_anno)
                    else:
                        return await function(obj_self, *args, **kwargs)

                caller = self._create_caller(function, sig, strict)
                fn_meta = FuncMeta(
                    async_wrapper,
                    invoke_handler=caller,
                    signature=sig,
                    stateless=stateless,
                    name=fn_name,
                    serve_with_agent=serve_with_agent,
                    is_async=True,
                )
                self.func_dict[fn_name] = fn_meta
                return fn_meta  # Return FuncMeta instance instead of wrapper

            else:
                @functools.wraps(function)
                def sync_wrapper(obj_self: "BaseObject", *args, **kwargs):
                    """
                    Wrapper function that handles remote/local method invocation.

                    Args:
                        obj_self: The object instance
                        *args: Positional arguments
                        **kwargs: Keyword arguments

                    Returns:
                        The result of the function call or a response object
                    """
                    if obj_self.remote:
                        if stateless:
                            req = self._extract_request(
                                obj_self, fn_name, args, kwargs, stateless, sig
                            )
                            resp = obj_self.session.fn_rpc(req)
                        else:
                            req = self._extract_request(
                                obj_self, fn_name, args, kwargs, stateless, sig
                            )
                            resp = obj_self.session.obj_rpc(req)
                        # Raise on non-OK status
                        if resp.status != int(InvocationResponseCode.Okay):
                            try:
                                details = json.loads(resp.payload.decode()) if resp.payload else {}
                            except Exception:
                                details = {'error_message': resp.payload.decode(errors='ignore')}
                            err_type = details.get('error_type') or 'Exception'
                            err_msg = details.get('error_message') or details.get('last_error') or str(details)
                            # Resolve to SDK-specific exception when possible
                            exc_cls = None
                            try:
                                from oaas_sdk2_py.simplified import errors as _sdk_errors  # type: ignore
                                exc_cls = getattr(_sdk_errors, err_type, None)
                            except Exception:
                                exc_cls = None
                            if exc_cls is None:
                                exc_cls = getattr(builtins, err_type, Exception)
                            raise exc_cls(err_msg)
                        # Map payload to annotated return type using UnifiedSerializer
                        ret_anno = sig.return_annotation
                        if ret_anno is inspect._empty or ret_anno is None:
                            # Best-effort decode for unannotated returns: provide attribute-style access
                            if not resp.payload:
                                return None
                            try:
                                from oaas_sdk2_py.simplified.serialization import UnifiedSerializer
                                _ser = UnifiedSerializer()
                                val = _ser.deserialize(resp.payload, Any)
                            except Exception:
                                try:
                                    val = json.loads(resp.payload.decode())
                                except Exception:
                                    return None
                            try:
                                from types import SimpleNamespace
                                def _to_attr(x):
                                    if isinstance(x, dict):
                                        return SimpleNamespace(**{k: _to_attr(v) for k, v in x.items()})
                                    if isinstance(x, list):
                                        return [ _to_attr(i) for i in x ]
                                    return x
                                return _to_attr(val)
                            except Exception:
                                return val
                        try:
                            if inspect.isclass(ret_anno) and issubclass(ret_anno, BaseModel):
                                return ret_anno.model_validate_json(resp.payload, strict=strict)
                        except Exception:
                            pass
                        if ret_anno is bytes:
                            return resp.payload
                        if ret_anno is str:
                            return resp.payload.decode()
                        from oaas_sdk2_py.simplified.serialization import UnifiedSerializer
                        _ser = UnifiedSerializer()
                        return _ser.deserialize(resp.payload, ret_anno)
                    else:
                        return function(obj_self, *args, **kwargs)

                caller = self._create_caller(function, sig, strict)
                fn_meta = FuncMeta(
                    sync_wrapper,
                    invoke_handler=caller,
                    signature=sig,
                    stateless=stateless,
                    name=fn_name,
                    serve_with_agent=serve_with_agent,
                )
                self.func_dict[fn_name] = fn_meta
                return fn_meta  # Return FuncMeta instance instead of wrapper
                
        return decorator

    def _extract_request(
        self, obj_self, fn_name, args, kwargs, stateless, sig: inspect.Signature
    ) -> InvocationRequest | ObjectInvocationRequest | None:
        """Extract or create a request object from function arguments.

        Enhanced to serialize the first user parameter using the method's
        type hint via UnifiedSerializer, supporting primitives and dicts.
        """
        # Try to find an existing request object
        req = self._find_request_object(args, kwargs)
        if req is not None:
            return req

        payload: bytes | None = None
        # Determine the first user parameter (beyond self)
        if len(sig.parameters) >= 2:
            second = list(sig.parameters.values())[1]
            param_name = second.name
            param_type = second.annotation
            # Pull value from args/kwargs
            if len(args) >= 1:
                arg_val = args[0]
            elif param_name in kwargs:
                arg_val = kwargs[param_name]
            else:
                arg_val = None
            # If still none, fallback to BaseModel scan for backward compatibility
            if arg_val is None:
                arg_val = self._find_base_model(args, kwargs)
            # Serialize if we have a value
            if arg_val is not None:
                from oaas_sdk2_py.simplified.serialization import UnifiedSerializer
                serializer = UnifiedSerializer()
                if param_type is inspect._empty:
                    payload = serializer.serialize(arg_val, None)
                else:
                    payload = serializer.serialize(arg_val, param_type)
        # Create appropriate request
        if stateless:
            return obj_self.create_request(fn_name, payload=payload)
        else:
            return obj_self.create_obj_request(fn_name, payload=payload)

    def _find_request_object(
        self, args, kwargs
    ) -> InvocationRequest | ObjectInvocationRequest | None:
        """Find InvocationRequest or ObjectInvocationRequest in args or kwargs."""
        # Check in args first
        for arg in args:
            if isinstance(arg, (InvocationRequest, ObjectInvocationRequest)):
                return arg

        # Then check in kwargs
        for _, val in kwargs.items():
            if isinstance(val, (InvocationRequest, ObjectInvocationRequest)):
                return val

        return None

    def _find_base_model(self, args, kwargs):
        """Find BaseModel instance in args or kwargs."""
        # Check in args first
        for arg in args:
            if isinstance(arg, BaseModel):
                return arg

        # Then check in kwargs
        for _, val in kwargs.items():
            if isinstance(val, BaseModel):
                return val

        return None

    def _create_request_from_model(
        self, obj_self: "BaseObject", fn_name: str, model: BaseModel, stateless: bool
    ):
        """Create appropriate request object from a BaseModel."""
        if model is None:
            if stateless:
                return obj_self.create_request(fn_name)
            else:
                return obj_self.create_obj_request(fn_name)
        payload = model.model_dump_json().encode()
        if stateless:
            return obj_self.create_request(fn_name, payload=payload)
        else:
            return obj_self.create_obj_request(fn_name, payload=payload)

    def _create_caller(self, function, sig: inspect.Signature, strict):
        """Create the appropriate caller function based on the signature."""
        param_count = len(sig.parameters)

        if param_count == 1:  # Just self
            return self._create_no_param_caller(function)
        elif param_count == 2:
            return self._create_single_param_caller(function, sig, strict)
        elif param_count == 3:
            return self._create_dual_param_caller(function, sig, strict)
        else:
            raise ValueError(f"Unsupported parameter count: {param_count}")

    def _create_no_param_caller(self, function):
        """Create caller for functions with no parameters."""
        sig = inspect.signature(function)
        
        if inspect.iscoroutinefunction(function):
            @functools.wraps(function)
            async def caller(obj_self, req):
                result = await function(obj_self)
                return parse_resp(result, sig.return_annotation)
            return caller
        else:
            @functools.wraps(function)
            def caller(obj_self, req):
                result = function(obj_self)
                return parse_resp(result, sig.return_annotation)
            return caller

    def _create_single_param_caller(self, function, sig: inspect.Signature, strict):
        """Create caller for functions with a single parameter using unified serialization."""
        second_param = list(sig.parameters.values())[1]
        param_type = second_param.annotation
        
        # Use unified serialization system for comprehensive type support
        # Lazy import to avoid circular imports
        from oaas_sdk2_py.simplified.serialization import UnifiedSerializer
        serializer = UnifiedSerializer()
        
        if inspect.iscoroutinefunction(function):
            @functools.wraps(function)
            async def caller(obj_self, req):
                try:
                    # Handle special cases first
                    if (param_type == InvocationRequest or param_type == ObjectInvocationRequest):
                        # Pass the request object directly
                        result = await function(obj_self, req)
                        return parse_resp(result, sig.return_annotation)
                    
                    # Deserialize with comprehensive type support
                    value = serializer.deserialize(req.payload, param_type)
                    result = await function(obj_self, value)
                    return parse_resp(result, sig.return_annotation)
                except Exception as e:
                    return self._create_error_response(e, param_type)
            return caller
        else:
            @functools.wraps(function)
            def caller(obj_self, req):
                try:
                    # Handle special cases first
                    if (param_type == InvocationRequest or param_type == ObjectInvocationRequest):
                        # Pass the request object directly
                        result = function(obj_self, req)
                        return parse_resp(result, sig.return_annotation)
                    
                    # Deserialize with comprehensive type support
                    value = serializer.deserialize(req.payload, param_type)
                    result = function(obj_self, value)
                    return parse_resp(result, sig.return_annotation)
                except Exception as e:
                    return self._create_error_response(e, param_type)
            return caller

    def _create_dual_param_caller(self, function, sig, strict):
        """Create caller for functions with model and request parameters."""
        second_param = list(sig.parameters.values())[1]
        model_cls = second_param.annotation
        
        # Use unified serialization system
        # Lazy import to avoid circular imports
        from oaas_sdk2_py.simplified.serialization import UnifiedSerializer
        serializer = UnifiedSerializer()

        if inspect.iscoroutinefunction(function):
            @functools.wraps(function)
            async def caller(obj_self, req):
                try:
                    # Deserialize using unified serializer for comprehensive type support
                    model = serializer.deserialize(req.payload, model_cls)
                    result = await function(obj_self, model, req)
                    return parse_resp(result, sig.return_annotation)
                except Exception as e:
                    return self._create_error_response(e, model_cls)
        else:
            @functools.wraps(function)
            def caller(obj_self, req):
                try:
                    # Deserialize using unified serializer for comprehensive type support
                    model = serializer.deserialize(req.payload, model_cls)
                    result = function(obj_self, model, req)
                    return parse_resp(result, sig.return_annotation)
                except Exception as e:
                    return self._create_error_response(e, model_cls)
        return caller

    def _create_error_response(self, error: Exception, param_type: type) -> InvocationResponse:
        """Create detailed error response for RPC serialization failures."""
        error_details = {
            'error_type': type(error).__name__,
            'parameter_type': param_type.__name__ if param_type else 'unknown',
            'error_message': str(error),
            'error_code': getattr(error, 'error_code', 'RPC_PARAM_ERROR'),
            'details': getattr(error, 'details', {})
        }
        
        return InvocationResponse(
            status=int(InvocationResponseCode.AppError),
            payload=json.dumps(error_details).encode()
        )

    def __str__(self):
        return "{" + f"name={self.name}, func_list={self.func_dict}" + "}"

    def export_pkg(self, pkg: dict) -> dict[str, Any]:
        # Build function bindings for this class per proposal
        fb_list = []
        for k, f in self.func_dict.items():
            fb_list.append({
                "name": k,
                "function_key": f"{self.name}.{k}",
                "access_modifier": "PUBLIC",
                "immutable": False,
                "parameters": []
            })

        # Optional: attempt to extract state/accessor metadata if present
        cls_entry = {
            "key": self.name,
            "description": getattr(getattr(self, 'cls', None), "__doc__", None) or "",
            "function_bindings": fb_list
        }

        # Accessors are not part of proposal's function_bindings, skip exporting separate accessors
        pkg["classes"].append(cls_entry)

        # Export functions list
        for k, f in self.func_dict.items():
            pkg["functions"].append({
                "key": f"{self.name}.{k}",
                "function_type": "CUSTOM",
                "description": getattr(f.func, "__doc__", None) or "",
                # Do not emit provision_config by default per proposal
                "config": {},
            })
        return pkg
