from fastapi import FastAPI
from pydantic import BaseModel
import time

## just for local dev use


class RequestSchema(BaseModel):
    user_id: str
    age: int


class ResponseSchema(BaseModel):
    greet: str


app = FastAPI()


@app.post("/hoge1")
def hoge1(req: RequestSchema) -> ResponseSchema:
    print("hoge1 called")
    time.sleep(3)
    print(req)
    return ResponseSchema(**{"greet": "Hi," + req.user_id + str(req.age)})


@app.post("/hoge2")
def hoge2(req: RequestSchema) -> ResponseSchema:
    print("hoge2 called")
    time.sleep(3)
    print(req)
    return ResponseSchema(**{"greet": "Hi," + req.user_id + str(req.age)})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)
