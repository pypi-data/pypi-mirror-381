import inspect
import typing as t
from contextlib import asynccontextmanager

from ellar.common import (
    IExecutionContext,
    IExecutionContextFactory,
    IGuardsConsumer,
    serialize_object,
)
from ellar.common.constants import (
    CONTROLLER_OPERATION_HANDLER_KEY,
    EXTRA_ROUTE_ARGS_KEY,
    NOT_SET,
)
from ellar.common.exceptions import WebSocketRequestValidationError
from ellar.common.logging import logger
from ellar.common.params import WebsocketEndpointArgsModel
from ellar.core.execution_context import current_config, current_injector
from ellar.reflect import reflect
from ellar.socket_io.context import GatewayContext
from ellar.socket_io.model import GatewayBase
from ellar.socket_io.responses import WsResponse
from ellar.utils import get_name
from socketio import AsyncServer
from starlette import status
from starlette.concurrency import run_in_threadpool
from starlette.exceptions import WebSocketException
from starlette.routing import compile_path

if t.TYPE_CHECKING:  # pragma: no cover
    from ellar.common.params import ExtraEndpointArg


class SocketOperationConnection:
    __slots__ = (
        "_event",
        "_server",
        "endpoint",
        "_name",
        "_is_coroutine",
        "endpoint_parameter_model",
        "controller",
    )

    ws_endpoint_args_model: t.Type[WebsocketEndpointArgsModel] = (
        WebsocketEndpointArgsModel
    )

    def __init__(
        self,
        controller: t.Type[GatewayBase],
        event: str,
        server: AsyncServer,
        message_handler: t.Callable,
    ) -> None:
        self._event = event
        self._server = server
        self.endpoint = message_handler
        self._name = get_name(self.endpoint)
        self._is_coroutine = inspect.iscoroutinefunction(message_handler)
        self.endpoint_parameter_model: WebsocketEndpointArgsModel = NOT_SET
        self.controller = controller
        self._load_model()
        self._register_handler()
        reflect.define_metadata(CONTROLLER_OPERATION_HANDLER_KEY, self, self.endpoint)

    @property
    def router_reflect_key(self) -> t.Any:
        return self.controller

    def _load_model(self) -> None:
        path_regex, path_format, param_convertors = compile_path("/")

        extra_route_args: t.Union[t.List["ExtraEndpointArg"], "ExtraEndpointArg"] = (
            reflect.get_metadata(EXTRA_ROUTE_ARGS_KEY, self.endpoint) or []
        )
        if not isinstance(extra_route_args, list):  # pragma: no cover
            extra_route_args = [extra_route_args]

        if self.endpoint_parameter_model is NOT_SET:
            self.endpoint_parameter_model = self.ws_endpoint_args_model(
                path=path_format,
                endpoint=self.endpoint,
                param_converters=param_convertors,
                extra_endpoint_args=extra_route_args,
            )
            self.endpoint_parameter_model.build_model()

    @asynccontextmanager
    async def catch(self, sid: t.Any) -> t.AsyncGenerator:
        try:
            yield
        except WebSocketException as aex:
            await self._handle_error(
                sid=sid,
                code=aex.code,
                reason=serialize_object(aex.reason),
            )
        except WebSocketRequestValidationError as wex:
            await self._handle_error(
                sid=sid,
                code=status.WS_1007_INVALID_FRAME_PAYLOAD_DATA,
                reason=serialize_object(wex.errors()),
            )
        except Exception as ex:
            await self._handle_error(
                sid=sid,
                code=status.WS_1011_INTERNAL_ERROR,
                reason=str(ex) if current_config.DEBUG else "Something went wrong",
            )

    async def _handle_error(self, sid: str, code: int, reason: t.Any) -> None:
        await self._server.emit("error", {"code": code, "reason": reason}, room=sid)
        await self._server.disconnect(sid=sid)

    async def handle(self, sid: str, gateway_instance: GatewayBase) -> t.Any:
        try:
            async with self.catch(sid=sid):
                await self.run_route_guards(context=gateway_instance.context)
                await self._run_handler(
                    context=gateway_instance.context, gateway_instance=gateway_instance
                )
        except Exception as ex:
            logger.exception(ex)
            raise ex

    async def _get_context(self, sid: str, environment: t.Dict) -> t.Any:
        execution_context_factory = current_injector.get(IExecutionContextFactory)
        context = execution_context_factory.create_context(
            operation=self,
            scope=environment["asgi.scope"],
            receive=environment["asgi.receive"],
            send=environment["asgi.send"],
        )

        return self._get_gateway_instance_and_context(ctx=context, sid=sid)

    def _register_handler(self) -> None:
        @self._server.on(self._event)
        async def _handler(sid: str, *environment: t.Any) -> t.Any:
            sid_environ = self._server.get_environ(sid)
            gateway_instance = await self._get_context(
                sid, environment[0] if len(environment) == 1 else sid_environ
            )
            await self.handle(sid, gateway_instance)

    async def _run_handler(
        self, context: IExecutionContext, gateway_instance: GatewayBase
    ) -> t.Any:
        resolver_result_ = await self.endpoint_parameter_model.resolve_dependencies(
            ctx=context
        )

        if gateway_instance.context.message:
            body_resolver_result_ = (
                await self.endpoint_parameter_model.resolve_ws_body_dependencies(
                    ctx=context, body_data=gateway_instance.context.message
                )
            )

            resolver_result_.data.update(body_resolver_result_.data)
            resolver_result_.errors.extend(body_resolver_result_.errors)

        if resolver_result_.errors:
            raise WebSocketRequestValidationError(resolver_result_.errors)
        if self._is_coroutine:
            res = await self.endpoint(gateway_instance, **resolver_result_.data)
        else:
            res = await run_in_threadpool(
                self.endpoint, gateway_instance, **resolver_result_.data
            )

        if res and isinstance(res, WsResponse):
            await self._server.emit(**res.dict())
        elif res:
            await self._server.emit(self._event, res)

    @t.no_type_check
    async def run_route_guards(self, context: GatewayContext) -> None:
        guard_consumer = context.get_service_provider().get(IGuardsConsumer)
        try:
            await guard_consumer.execute(context, self)
        except Exception:
            await self._server.emit(
                "error",
                {
                    "code": status.WS_1011_INTERNAL_ERROR,
                    "reason": "Authorization Failed",
                },
                room=context.sid,
            )
            await self._server.disconnect(sid=context.sid)

    def get_controller_type(self) -> t.Type[GatewayBase]:
        """
        For operation under a controller, `get_control_type` and `get_class` will return the same result
        For operation under ModuleRouter, this will return a unique type created for the router for tracking some properties
        :return: a type that wraps the operation
        """
        return t.cast(t.Type[GatewayBase], self.router_reflect_key)

    def _get_gateway_instance(self, ctx: IExecutionContext) -> GatewayBase:
        gateway_type = self.controller
        if not gateway_type or (
            gateway_type and not issubclass(gateway_type, GatewayBase)
        ):  # pragma: no cover
            raise RuntimeError("GatewayBase Type was not found")

        service_provider = ctx.get_service_provider()

        gateway_instance = service_provider.get(gateway_type)
        return t.cast(GatewayBase, gateway_instance)

    def _get_gateway_instance_and_context(
        self, ctx: IExecutionContext, sid: str, message: t.Any = None
    ) -> GatewayBase:
        sid_environ = self._server.get_environ(sid)
        gateway_instance = self._get_gateway_instance(ctx)
        gateway_instance.context = GatewayContext(
            server=self._server,
            context=ctx,
            sid=sid,
            environment=sid_environ,
            message=message,
        )
        return gateway_instance


class SocketMessageOperation(SocketOperationConnection):
    async def _get_context(self, sid: str, message: t.Any) -> t.Any:
        sid_environ = self._server.get_environ(sid)

        execution_context_factory = current_injector.get(IExecutionContextFactory)
        context = execution_context_factory.create_context(
            operation=self,
            scope=sid_environ["asgi.scope"],
            receive=sid_environ["asgi.receive"],
            send=sid_environ["asgi.send"],
        )

        return self._get_gateway_instance_and_context(
            ctx=context, sid=sid, message=message
        )

    def _register_handler(self) -> None:
        @self._server.on(self._event)
        async def _handler(sid: str, message: t.Any = None) -> t.Any:
            gateway_instance = await self._get_context(sid, message)
            await self.handle(sid, gateway_instance)
