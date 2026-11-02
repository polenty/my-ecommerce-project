import pytest

from cart import ShoppingCart
from product import Product


@pytest.fixture
def cart():
    return ShoppingCart([
        Product("phone", "Смартфон", 1000, 5),
        Product("case", "Чехол", 10, 10),
    ])


# ----- добавление -----
def test_add_item(cart):
    cart.add_item("phone", 2)
    assert cart.items == {"phone": 2}


def test_add_item_twice(cart):
    cart.add_item("phone", 2)
    cart.add_item("phone", 1)
    assert cart.items == {"phone": 3}


def test_add_zero(cart):
    with pytest.raises(ValueError):
        cart.add_item("phone", 0)


def test_add_negative(cart):
    with pytest.raises(ValueError):
        cart.add_item("phone", -1)


def test_add_unknown_product(cart):
    with pytest.raises(ValueError):
        cart.add_item("tv", 1)


def test_add_more_than_stock(cart):
    with pytest.raises(ValueError):
        cart.add_item("phone", 6)


def test_add_more_than_stock_with_cart(cart):
    cart.add_item("phone", 4)
    with pytest.raises(ValueError):
        cart.add_item("phone", 2)


# ----- удаление -----
def test_remove_all(cart):
    cart.add_item("phone", 3)
    cart.remove_item("phone")
    assert cart.items == {}


def test_remove_part(cart):
    cart.add_item("phone", 3)
    cart.remove_item("phone", 1)
    assert cart.items == {"phone": 2}


def test_remove_more_than_have(cart):
    cart.add_item("phone", 2)
    cart.remove_item("phone", 5)
    assert cart.items == {}


def test_remove_missing_item(cart):
    with pytest.raises(ValueError):
        cart.remove_item("phone")


def test_remove_zero(cart):
    cart.add_item("phone", 2)
    with pytest.raises(ValueError):
        cart.remove_item("phone", 0)


# ----- стоимость -----
def test_total_empty(cart):
    assert cart.get_total() == 0


def test_total(cart):
    cart.add_item("phone", 2)
    cart.add_item("case", 3)
    assert cart.get_total() == 2030


def test_total_with_promo(cart):
    cart.add_item("phone", 2)
    assert cart.get_total("SAVE10") == 1800


def test_total_wrong_promo(cart):
    cart.add_item("phone", 1)
    with pytest.raises(ValueError):
        cart.get_total("FAKE")

def test_total_with_promo_50(cart):
    cart.add_item("phone", 2)
    assert cart.get_total("SAVE50") == 1000