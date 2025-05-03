from typing import Any
from unittest.mock import MagicMock, patch
import pytest
from src.product import Product


def test_product_init(samsung_product: Product, iphone_product: Product) -> None:
    assert samsung_product.name == "Samsung Galaxy S23 Ultra"
    assert samsung_product.description == "256GB, Серый цвет, 200MP камера"
    assert samsung_product.price == 180000.0
    assert samsung_product.quantity == 5


def test_new_product() -> None:
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


def test_new_product_not_in_list() -> None:
    new_product = Product.new_product(
        {
            "name": "Samsung",
            "description": "256GB",
            "price": 180.0,
            "quantity": 5,
        }
    )
    assert new_product.name == "Samsung"
    assert new_product.description == "256GB"
    assert new_product.price == 180.0
    assert new_product.quantity == 5


def test_price_setter(samsung_product: Product) -> None:
    samsung_product.price = 200000.0
    assert samsung_product.price == 200000.0


@patch("builtins.input", side_effect="y")
def test_price_setter_reduce(mock_input: MagicMock) -> None:
    test_product = Product("Test_name", "250gb", 150.0, 2)
    test_product.price = 100.0
    assert test_product.price == 100.0


@patch("builtins.input", side_effect="n")
def test_price_setter_no_reduce(mock_input: MagicMock) -> None:
    test_product = Product("Test_name", "250gb", 150.0, 2)
    test_product.price = 100.0
    assert test_product.price == 150.0


def test_price_zero_setter(capsys: Any, samsung_product: Product) -> None:
    samsung_product.price = 0
    captured = capsys.readouterr()
    assert captured.out.strip().split("\n")[-1] == "Цена не должна быть нулевая или отрицательная"


def test_product_str(samsung_product: Product) -> None:
    assert str(samsung_product) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_product_add(samsung_product: Product, iphone_product: Product) -> None:
    assert samsung_product + iphone_product == 2580000


def test_product_with_zero_quantity() -> None:
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product(name="Samsung23", description="256GB, Серый цвет", price=180.0, quantity=0)
