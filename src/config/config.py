from pydantic import BaseSettings
from typing import Dict
import os


class Settings(BaseSettings):
    host = os.getenv("UNDERLYING_HOST", default="localhost")

    SALT: str = "XXX"
    RATIO: Dict[str, float] = {
        f"http://{host}:8001/hoge1": 0.3,
        f"http://{host}:8001/hoge2": 0.7,
    }


settings = Settings()
