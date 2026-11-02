from product import Product


def test_product():
    p = Product("prod_102", "Смартфон", 1000, 5)
    assert p.id == "prod_102"
    assert p.name == "Смартфон"
    assert p.price == 1000
    assert p.stock == 5