from model.request_schema import RequestSchema
from typing import Dict, Any
from service.http_client_wrapper import HttpClientWrapper
from service.logging_service import LoggingService
from service.routing_service import RoutingService


class ProxyService:
    def __init__(
        self,
        http_client_wrapper: HttpClientWrapper,
        routing_service: RoutingService,
        logging_service: LoggingService,
    ):
        self.http_client_wrapper: HttpClientWrapper = http_client_wrapper
        self.routing_service: RoutingService = routing_service
        self.logging_service: LoggingService = logging_service

    async def route_and_post(self, req: RequestSchema) -> Dict[str, Any]:
        seed = req.get_seed()
        original = req.original

        url = self.routing_service.find_route(seed)
        r = await self.http_client_wrapper.post(url, original)
        self.logging_service.publish(seed, url, r)
        return r
