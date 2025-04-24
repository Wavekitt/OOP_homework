class PrintMixin:
    """
    Класс-миксин для печати в консоль информации об экземпляре класса.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(repr(self))

    def __repr__(self):
        return (f"{self.__class__.__name__}({self.name}, {self.description}, "
                f"{self.price}, {self.quantity})")
