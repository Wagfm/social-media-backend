from collections.abc import Iterable
from dataclasses import dataclass, fields, asdict
from typing import Self, Any


@dataclass(frozen=True)
class BaseModel:
    @classmethod
    def from_dict(cls, data: dict) -> Self:
        valid_fields = [field.name for field in fields(cls)]
        valid_data = {field: data[field] for field in valid_fields}
        return cls(**valid_data)

    def to_dict(self, exclude_none=False) -> dict[str, Any]:
        data = asdict(self)
        if not exclude_none:
            return data
        return {key: value for key, value in data if value is not None}

    @classmethod
    def get_fields(cls) -> Iterable[str]:
        return [field.name for field in fields(cls)]
