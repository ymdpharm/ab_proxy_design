from typing import Dict
from exception.config_error import InvalidRoutingConfigError
import hashlib


class RoutingService:
    def __init__(self, salt: str, ratio: Dict[str, float]):
        if sum(ratio.values()) != 1:
            raise InvalidRoutingConfigError("ratio sum is not 1")

        self.ratio = ratio
        self.salt = salt
        self.hash_algorithm = hashlib.sha512
        self.hash_size = self.hash_algorithm().digest_size

    def find_route(self, seed: str):
        hash = self._get_hash(seed)
        print(hash)
        cum = 0
        for k, v in self.ratio.items():
            cum += v
            if hash <= cum:
                return k
        return list(self.ratio.keys())[0]  # unreachable..

    def _get_hash(self, seed: str):
        salted_seed = (self.salt + seed).encode("utf-8")
        digest = self.hash_algorithm(salted_seed).digest()
        hash_int = int.from_bytes(digest, "big")
        size = 2 ** (self.hash_size * 8)
        return hash_int / size
