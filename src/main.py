from fastapi import FastAPI
from model.request_schema import RequestSchema
from service.http_client_wrapper import HttpClientWrapper
from service.proxy_service import ProxyService
from service.routing_service import RoutingService
from typing import Dict, Any


app = FastAPI()

## composition with vanilla DI
http_client_wrapper = HttpClientWrapper()
logging_service = ...  ## todo: impl
routing_service = RoutingService(
    "salt", {"http://localhost:8001/hoge1": 0.3, "http://localhost:8001/hoge2": 0.7}
)  ## todo: make conf
proxy_service = ProxyService(http_client_wrapper, routing_service)


@app.post("/hoge")
def hoge(req: RequestSchema) -> Dict[str, Any]:
    return proxy_service.route_and_post(req)


## todo: error handling

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)