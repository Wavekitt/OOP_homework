from typing import Type, Any

from src.product import Product


def test_product_init(
    samsung_product: Type[Product], iphone_product: Type[Product]
) -> None:

    assert samsung_product.name == "Samsung Galaxy S23 Ultra"
    assert samsung_product.description == "256GB, Серый цвет, 200MP камера"
    assert samsung_product.price == 180000.0


def test_new_product() -> None:
    """Тест проверяет корректное создание нового экземпляра класса Product из словаря данных."""
    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 180000.0
    assert new_product.quantity == 5


def test_price_setter(samsung_product: Type[Product]) -> None:
    """Тест проверяет корректное изменение цены у продукта, если цена задана выше 0."""
    samsung_product.price = 100.0
    assert samsung_product.price == 100.0


def test_price_zero_setter(capsys: Any, samsung_product: Type[Product]) -> None:
    """Тест проверяет корректный возврат сообщение, если заданная цена меньше или равна 0."""
    samsung_product.price = 0
    captured = capsys.readouterr()
    assert captured.out == "Цена не должна быть нулевая или отрицательная\n"
