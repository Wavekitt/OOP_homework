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
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str

    @property
    def products_in_list(self) -> list:
        """
        Геттер выводит список товаров.
        """
        return self.__products
