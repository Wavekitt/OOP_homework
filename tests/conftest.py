from typing import Any

import pytest

from src.category import Category
from src.product import Product
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass


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


@pytest.fixture
def smartphone_product() -> Any:
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def smartphone_product_another() -> Any:
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def lawn_grass() -> Any:
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def lawn_grass_another() -> Any:
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")


@pytest.fixture
def category_without_product() -> Any:
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получения дополнительных функций",
        products=[],
    )
