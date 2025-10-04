import functools
import typing as t
from types import FunctionType

from ellar.common.constants import (
    DELETE,
    GET,
    HEAD,
    OPERATION_ENDPOINT_KEY,
    OPTIONS,
    PATCH,
    POST,
    PUT,
    ROUTE_OPERATION_PARAMETERS,
    TRACE,
)
from ellar.common.interfaces.operation import IWebSocketConnectionAttributes
from ellar.reflect import ensure_target

from .schema import RouteParameters, WsRouteParameters


def _websocket_connection_attributes(
    func: t.Callable,
) -> IWebSocketConnectionAttributes:
    def _advance_function(
        websocket_handler: t.Callable, handler_name: str
    ) -> t.Callable:
        def _wrap(connect_handler: t.Callable) -> t.Callable:
            if not (
                callable(websocket_handler) and type(websocket_handler) is FunctionType
            ):
                raise Exception(
                    "Invalid type. Please make sure you passed the websocket handler."
                )

            _item: t.Optional[WsRouteParameters] = getattr(
                websocket_handler, ROUTE_OPERATION_PARAMETERS, None
            )

            if not _item or not isinstance(_item, WsRouteParameters):
                raise Exception(
                    "Invalid type. Please make sure you passed the websocket handler."
                )

            _item.add_websocket_handler(
                handler_name=handler_name, handler=connect_handler
            )

            return connect_handler

        return _wrap

    func.connect = functools.partial(_advance_function, handler_name="on_connect")  # type: ignore[attr-defined]
    func.disconnect = functools.partial(_advance_function, handler_name="on_disconnect")  # type: ignore[attr-defined]

    return t.cast(IWebSocketConnectionAttributes, func)


class OperationDefinitions:
    """Defines HTTP and WebSocket route operations for the Ellar framework.

    This class provides decorators for defining different types of route handlers:
    - HTTP methods (GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS, TRACE)
    - Generic HTTP routes with custom methods
    - WebSocket routes with connection handling

    Each route decorator registers the endpoint with appropriate parameters and
    metadata for the framework to process requests.

    Example:
        ```python
        from ellar.common import get, post, ws_route

        @get("/users")
        def get_users():
            return {"users": [...]}

        @post("/users")
        def create_user(user_data: dict):
            return {"status": "created"}

        @ws_route("/ws")
        def websocket_handler():
            # Handle WebSocket connections
            pass
        ```
    """

    __slots__ = ()

    def _get_operation(self, route_parameter: RouteParameters) -> t.Callable:
        endpoint = ensure_target(route_parameter.endpoint)
        setattr(endpoint, OPERATION_ENDPOINT_KEY, True)
        route_parameters = getattr(endpoint, ROUTE_OPERATION_PARAMETERS, [])
        route_parameters.append(route_parameter)
        setattr(endpoint, ROUTE_OPERATION_PARAMETERS, route_parameters)

        return route_parameter.endpoint

    def _get_ws_operation(self, ws_route_parameters: WsRouteParameters) -> t.Callable:
        endpoint = ensure_target(ws_route_parameters.endpoint)

        setattr(endpoint, OPERATION_ENDPOINT_KEY, True)
        setattr(
            endpoint,
            ROUTE_OPERATION_PARAMETERS,
            ws_route_parameters,
        )
        return ws_route_parameters.endpoint

    def _get_decorator_or_operation(
        self, path: t.Union[str, t.Callable], endpoint_parameter_partial: t.Callable
    ) -> t.Callable:
        if callable(path):
            route_parameter = endpoint_parameter_partial(endpoint=path, path="/")
            self._get_operation(route_parameter=route_parameter)
            return path

        def _decorator(endpoint_handler: t.Callable) -> t.Callable:
            _route_parameter = endpoint_parameter_partial(
                endpoint=endpoint_handler, path=path
            )
            self._get_operation(route_parameter=_route_parameter)
            return endpoint_handler

        return _decorator

    def get(
        self,
        path: str = "/",
        *,
        name: t.Optional[str] = None,
        include_in_schema: bool = True,
        response: t.Union[
            t.Dict[int, t.Type], t.List[t.Tuple[int, t.Type]], t.Type, t.Any
        ] = None,
    ) -> t.Callable:
        methods = [GET]
        endpoint_parameter_partial = functools.partial(
            RouteParameters,
            name=name,
            methods=methods,
            include_in_schema=include_in_schema,
            response=response,
        )
        return self._get_decorator_or_operation(path, endpoint_parameter_partial)

    def post(
        self,
        path: str = "/",
        *,
        name: t.Optional[str] = None,
        include_in_schema: bool = True,
        response: t.Union[
            t.Dict[int, t.Type], t.List[t.Tuple[int, t.Type]], t.Type, t.Any
        ] = None,
    ) -> t.Callable:
        methods = [POST]
        endpoint_parameter_partial = functools.partial(
            RouteParameters,
            name=name,
            methods=methods,
            include_in_schema=include_in_schema,
            response=response,
        )
        return self._get_decorator_or_operation(path, endpoint_parameter_partial)

    def put(
        self,
        path: str = "/",
        *,
        name: t.Optional[str] = None,
        include_in_schema: bool = True,
        response: t.Union[
            t.Dict[int, t.Type], t.List[t.Tuple[int, t.Type]], t.Type, t.Any
        ] = None,
    ) -> t.Callable:
        methods = [PUT]
        endpoint_parameter_partial = functools.partial(
            RouteParameters,
            name=name,
            methods=methods,
            include_in_schema=include_in_schema,
            response=response,
        )
        return self._get_decorator_or_operation(path, endpoint_parameter_partial)

    def patch(
        self,
        path: str = "/",
        *,
        name: t.Optional[str] = None,
        include_in_schema: bool = True,
        response: t.Union[
            t.Dict[int, t.Type], t.List[t.Tuple[int, t.Type]], t.Type, t.Any
        ] = None,
    ) -> t.Callable:
        methods = [PATCH]
        endpoint_parameter_partial = functools.partial(
            RouteParameters,
            name=name,
            methods=methods,
            include_in_schema=include_in_schema,
            response=response,
        )
        return self._get_decorator_or_operation(path, endpoint_parameter_partial)

    def delete(
        self,
        path: str = "/",
        *,
        name: t.Optional[str] = None,
        include_in_schema: bool = True,
        response: t.Union[
            t.Dict[int, t.Type], t.List[t.Tuple[int, t.Type]], t.Type, t.Any
        ] = None,
    ) -> t.Callable:
        methods = [DELETE]
        endpoint_parameter_partial = functools.partial(
            RouteParameters,
            name=name,
            methods=methods,
            include_in_schema=include_in_schema,
            response=response,
        )
        return self._get_decorator_or_operation(path, endpoint_parameter_partial)

    def head(
        self,
        path: str = "/",
        *,
        name: t.Optional[str] = None,
        include_in_schema: bool = True,
        response: t.Union[
            t.Dict[int, t.Type], t.List[t.Tuple[int, t.Type]], t.Type, t.Any
        ] = None,
    ) -> t.Callable:
        methods = [HEAD]
        endpoint_parameter_partial = functools.partial(
            RouteParameters,
            name=name,
            methods=methods,
            include_in_schema=include_in_schema,
            response=response,
        )
        return self._get_decorator_or_operation(path, endpoint_parameter_partial)

    def options(
        self,
        path: str = "/",
        *,
        name: t.Optional[str] = None,
        include_in_schema: bool = True,
        response: t.Union[
            t.Dict[int, t.Type], t.List[t.Tuple[int, t.Type]], t.Type, t.Any
        ] = None,
    ) -> t.Callable:
        methods = [OPTIONS]
        endpoint_parameter_partial = functools.partial(
            RouteParameters,
            name=name,
            methods=methods,
            include_in_schema=include_in_schema,
            response=response,
        )
        return self._get_decorator_or_operation(path, endpoint_parameter_partial)

    def trace(
        self,
        path: str = "/",
        *,
        name: t.Optional[str] = None,
        include_in_schema: bool = True,
        response: t.Union[
            t.Dict[int, t.Type], t.List[t.Tuple[int, t.Type]], t.Type, t.Any
        ] = None,
    ) -> t.Callable:
        methods = [TRACE]
        endpoint_parameter_partial = functools.partial(
            RouteParameters,
            name=name,
            methods=methods,
            include_in_schema=include_in_schema,
            response=response,
        )
        return self._get_decorator_or_operation(path, endpoint_parameter_partial)

    def http_route(
        self,
        path: str = "/",
        *,
        methods: t.List[str],
        name: t.Optional[str] = None,
        include_in_schema: bool = True,
        response: t.Union[
            t.Dict[int, t.Type], t.List[t.Tuple[int, t.Type]], t.Type, t.Any
        ] = None,
    ) -> t.Callable:
        def _decorator(endpoint_handler: t.Callable) -> t.Callable:
            endpoint_parameter = RouteParameters(
                name=name,
                path=path,
                methods=methods,
                include_in_schema=include_in_schema,
                response=response,
                endpoint=endpoint_handler,
            )
            self._get_operation(route_parameter=endpoint_parameter)
            return endpoint_handler

        return _decorator

    @_websocket_connection_attributes
    def ws_route(
        self,
        path: str = "/",
        *,
        name: t.Optional[str] = None,
        encoding: t.Optional[str] = "json",
        use_extra_handler: bool = False,
        extra_handler_type: t.Optional[t.Type] = None,
    ) -> t.Callable:
        def _decorator(
            endpoint_handler: t.Callable,
        ) -> t.Callable:
            endpoint_parameter = WsRouteParameters(
                name=name,
                path=path,
                endpoint=endpoint_handler,
                encoding=encoding,
                use_extra_handler=use_extra_handler,
                extra_handler_type=extra_handler_type,
            )
            self._get_ws_operation(ws_route_parameters=endpoint_parameter)
            return endpoint_handler

        return _decorator
