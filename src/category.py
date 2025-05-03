from typing import Any
from src.product import Product


class Category:
    """
    Класс для представления категории продукта.
    """

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        """
        Метод для инициализации экземпляра класса Category. Задаем значения атрибутам экземпляра.
        """
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self) -> str:
        product_quantity = 0
        for product in self.__products:
            product_quantity += product.quantity
        return f"{self.name}, количество продукта: {product_quantity} шт."

    def add_product(self, product: Product) -> None:
        """
        Метод добавляет новый экземпляр класса Product в приватный список продуктов.
        """
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            print("Неверный тип")

    @property
    def products(self) -> str:
        """
        Геттер выводит список товаров в виде строк.
        """
        products_str = ""
        for product in self.__products:
            products_str += f"{Product.__str__(product)}\n"
        return products_str

    @property
    def products_in_list(self) -> list:
        """
        Геттер выводит список товаров.
        """
        return self.__products

    def middle_price(self) -> Any:
        """
        Метод подсчитывает средний ценник всех товаров.
        """
        try:
            return round(sum([product.price for product in self.__products]) / len(self.__products), 2)
        except ZeroDivisionError:
            return 0
