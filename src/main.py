from fastapi import FastAPI
from model.request_schema import RequestSchema
from service.http_client_wrapper import AsyncHttpClientWrapper
from service.logging_service import LoggingService
from service.proxy_service import ProxyService
from service.routing_service import RoutingService
from config.config import settings
from typing import Dict, Any
import httpx, logging

app = FastAPI()

## composition with vanilla DI
http_client_wrapper = AsyncHttpClientWrapper(httpx.AsyncClient())
logging_service = LoggingService(logging.getLogger("uvicorn"))
routing_service = RoutingService(settings.SALT, settings.RATIO)
proxy_service = ProxyService(http_client_wrapper, routing_service, logging_service)


@app.post("/hoge")
async def hoge(req: RequestSchema) -> Dict[str, Any]:
    return await proxy_service.route_and_post(req)


@app.on_event("shutdown")
async def shutdown():
    return await http_client_wrapper.close()


## todo: error handling

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
