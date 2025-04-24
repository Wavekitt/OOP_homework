from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    """Абстрактный класс BaseProduct. В нем реализован класс-метод для добавления нового продукта."""

    @classmethod
    @abstractmethod
    def new_product(cls, *args: Any, **kwargs: Any) -> Any:
        """Абстрактный метод для добавления нового продукта класса."""
        pass
