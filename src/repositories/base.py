from abc import abstractmethod
from collections.abc import Iterable
from typing import Protocol, Any

from models.base import BaseModel


class BaseRepository(Protocol):
    @abstractmethod
    def create(self, data: dict[str, Any]) -> BaseModel:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id: Any) -> BaseModel:
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> Iterable[BaseModel]:
        raise NotImplementedError

    @abstractmethod
    def update(self, data: dict[str, Any]) -> BaseModel:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: Any) -> BaseModel:
        raise NotImplementedError
