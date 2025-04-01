class Product:
    """Класс для представления продукта."""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Метод для инициализации экземпляра класса Product. Задаем значения атрибутам экземпляра."""

        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
