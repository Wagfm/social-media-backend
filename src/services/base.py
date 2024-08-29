from abc import abstractmethod
from collections.abc import Iterable
from typing import Protocol, Any

from dtos.base import BaseDto


class BaseService(Protocol):
    @abstractmethod
    def create(self, dto: BaseDto) -> BaseDto:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id: Any) -> BaseDto:
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> Iterable[BaseDto]:
        raise NotImplementedError

    @abstractmethod
    def update(self, id: Any, dto: BaseDto) -> BaseDto:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: Any) -> BaseDto:
        raise NotImplementedError
