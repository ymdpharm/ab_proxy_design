from typing import Dict, Any
from pytz import utc
import logging, datetime


class LoggingService:
    def __init__(self, logger):
        self.logger = logger

    def publish(self, seed: str, url: str, result: Dict[str, Any]):
        self.logger.info(self._fmt(seed, url, result))

    def _fmt(self, seed: str, url: str, result: Dict[str, Any]):
        dt = datetime.datetime.now(utc)
        return {
            "seed": seed,
            "allocated": url,
            "timestamp": f"{dt:%Y-%m-%dT%H:%M:%S%z}",
            "result": result,
        }
