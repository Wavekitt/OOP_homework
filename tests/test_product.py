from typing import Type

from src.product import Product


def test_product_init(
    samsung_product: Type[Product], iphone_product: Type[Product]
) -> None:

    assert samsung_product.name == "Samsung Galaxy S23 Ultra"
    assert samsung_product.description == "256GB, Серый цвет, 200MP камера"
    assert samsung_product.price == 180000.0
