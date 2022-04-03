from model.request_schema import RequestSchema
from typing import Dict, Any
from service.http_client_wrapper import HttpClientWrapper
from service.routing_service import RoutingService


class ProxyService:
    def __init__(
        self, http_client_wrapper: HttpClientWrapper, routing_service: RoutingService
    ):
        self.http_client_wrapper: HttpClientWrapper = http_client_wrapper
        self.routing_service: RoutingService = routing_service

    def route_and_post(self, req: RequestSchema) -> Dict[str, Any]:
        url = self.routing_service.find_route(req.get_seed())
        return self.http_client_wrapper.post(url, req.original)
