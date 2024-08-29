from abc import abstractmethod
from collections.abc import Iterable
from typing import Protocol, Any


class BaseRepository[T](Protocol):
    @abstractmethod
    def create(self, data: dict[str, Any]) -> T:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id: Any) -> T:
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> Iterable[T]:
        raise NotImplementedError

    @abstractmethod
    def update(self, data: dict[str, Any]) -> T:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: Any) -> T:
        raise NotImplementedError
