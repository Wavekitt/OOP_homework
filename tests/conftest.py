from typing import Any

import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def samsung_product() -> Any:
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
    )


@pytest.fixture
def iphone_product() -> Any:
    return Product(
        name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8
    )


@pytest.fixture
def smartphone_category() -> Any:
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получения дополнительных функций",
        products=[
            Product(
                "Samsung Galaxy S23 Ultra",
                "256GB, Серый цвет, 200MP камера",
                180000.0,
                5,
            ),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
            Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
        ],
    )


@pytest.fixture
def tv_category() -> Any:
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром",
        products=[Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)])
