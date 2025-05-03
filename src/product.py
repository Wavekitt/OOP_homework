from typing import Any
from src.product_base import BaseProduct
from src.mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    """
    Класс для представления продукта.
    Класс содержит следующие свойства: название (name: str), описание (description: str), цена(__price: float),
    количество в наличии(quantity: int)
    """
    name: str
    description: str
    price: float
    quantity: int
    product_list: list = []

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Метод для инициализации экземпляра класса Product. Задаем значения атрибутам экземпляра. Добавляет
        экземпляр класса в список продуктов.
        """

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        if quantity != 0:
            self.quantity = quantity
        else:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.product_cost = price * quantity
        super().__init__()

        if self.check_product_list(name, price, quantity):

            self_product = {"name": name, "description": description, "price": price, "quantity": quantity}
            Product.product_list.append(self_product)

    def __str__(self) -> str:
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Any) -> Any:
        """
        Метод возвращает полную стоимость всех товаров на складе выбранной категории товаров.
        """
        if type(other) is self.__class__:
            return self.product_cost + other.product_cost
        else:
            raise TypeError

    @staticmethod
    def check_product_list(name: str, price: float, quantity: int) -> bool:

        """
        Статическй метод проверяет наличие товара по переданному имени. Если имя существует, то суммирует кол-во
        и устанавливает максимальную цену. Если имя не найдено, то возвращает True-знак для добавления товара в
        список.
        """

        for product in Product.product_list:
            if name == product.get("name", ""):
                product["quantity"] += quantity
                product["price"] = max(product["price"], price)
                return False

        return True

    @classmethod
    def new_product(cls, product_date: dict) -> Any:
        """
        Класс-метод принимает на вход параметры товара в словаре и возвращает объект класса Product. Также проверяет
        наличие данного товара в списке по имени. Если такого товара нет, то добавляет его в список. Иначе суммирует
        кол-во товара и устанавливает максимальную цену.
        """

        name = product_date.get("name", "Нет названия")
        description = product_date.get("description", "Нет описания")
        price = product_date.get("price", 0.0)
        quantity = product_date.get("quantity", 0)

        if cls.check_product_list(name, price, quantity):
            cls_product = {"name": name, "description": description, "price": price, "quantity": quantity}
            Product.product_list.append(cls_product)
            return cls(**product_date)
        else:
            return cls(**product_date)

    @property
    def price(self) -> float:
        """
        Геттер возвращает цену за выбранный товар.
        """

        return self.__price

    @price.setter
    def price(self, update_price: int) -> None:
        """
        Сеттер обновляет цену товара. Если цена товара равна или меньше 0, то выводит сообщение об ошибке.
        Если цена товара меньше установленной, то спрашивает у пользователя подтверждение замены цены и обновляет цену
        в случае согласия пользователя. Если цена выше установленной, то обновляет цену.
        """

        if update_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        elif update_price < self.__price:
            confirm_message = input("Понизить цену товара? (y: yes / любой другой ответ: no):")
            if confirm_message == "y":
                self.__price = update_price
            else:
                return
        else:
            self.__price = update_price
