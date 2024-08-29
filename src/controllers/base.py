from abc import abstractmethod
from typing import Protocol, Any

from fastapi import Response

from dtos.base import BaseDto


class BaseController(Protocol):
    @abstractmethod
    def create(self, dto: BaseDto, response: Response) -> Response:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id: Any, response: Response) -> Response:
        raise NotImplementedError

    @abstractmethod
    def get_all(self, response: Response) -> Response:
        raise NotImplementedError

    @abstractmethod
    def update(self, id: Any, dto: BaseDto, response: Response) -> Response:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: Any, response: Response) -> Response:
        raise NotImplementedError
