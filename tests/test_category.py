from src.category import Category
from src.product import Product


def test_category_init(smartphone_category: Category, tv_category: Category) -> None:
    assert smartphone_category.name == "Смартфоны"
    assert (
        smartphone_category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций"
    )

    assert tv_category.name == "Телевизоры"
    assert tv_category.description == "Современный телевизор, который позволяет наслаждаться просмотром"

    assert smartphone_category.category_count == 2
    assert tv_category.category_count == 2

    assert smartphone_category.product_count == 4
    assert tv_category.product_count == 4


def test_category_add_product(smartphone_category: Category) -> None:
    new_product = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    assert len(smartphone_category.products_in_list) == 3
    smartphone_category.add_product(new_product)
    assert len(smartphone_category.products_in_list) == 4


def test_category_products_getter(smartphone_category: Category) -> None:
    assert smartphone_category.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )


def test_category_str(smartphone_category: Category) -> None:
    assert str(smartphone_category) == "Смартфоны, количество продукта: 27 шт."
