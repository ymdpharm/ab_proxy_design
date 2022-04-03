from pydantic import BaseModel, root_validator
from typing import Dict, Any


class RequestSchema(BaseModel):
    """
    Validate only that seed field is present.
    Whole body is set as original, without any validations.
    """

    user_id: str
    original: Dict[str, Any]

    @root_validator(pre=True)
    def build_original(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        values["original"] = values.copy()
        return values

    def get_seed(self) -> str:
        return self.user_id  # define field to be used as seed.
