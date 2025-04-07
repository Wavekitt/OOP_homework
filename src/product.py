from typing import Any


class Product:
    """
    Класс для представления продукта.
    """

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Метод для инициализации экземпляра класса Product. Задаем значения атрибутам экземпляра.
        """

        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_date: dict) -> Any:
        """
        Класс-метод принимает на вход параметры товара в словаре и возвращает объект класса Product.
        """
        name = product_date.get("name", "Нет названия")
        description = product_date.get("description", "Нет описания")
        price = product_date.get("price", 0.0)
        quantity = product_date.get("quantity", 0)

        return cls(name, description, price, quantity)

    @property
    def price(self) -> float:
        """
        Геттер возвращает цену за выбранный товар.
        """
        return self.__price

    @price.setter
    def price(self, update_price: int) -> None:
        """
        Сеттер обновляет цену товара, если переданная цена больше 0.
        """
        if update_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        self.__price = update_price
