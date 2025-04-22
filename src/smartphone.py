from src.product import Product


class Smartphone(Product):
    """
    Класс-наследник для представления продукта категории смартфон.
    """

    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        """
        Метод для инициализации экземпляра класса Smartphone. Задает значения атрибутам экземпляра. Добавляет
        экземпляр класса в список продуктов.
        """
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
