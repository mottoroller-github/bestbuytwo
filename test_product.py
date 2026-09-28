from products import Product
import pytest

def test_creating_prod():
    product = Product("MacBook Air M2", price=1450, quantity=100)

    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100
    assert product.is_active() is True

def test_creating_prod_invalid_details():
    # Empty name
    with pytest.raises(Exception):
        Product("", price=1450, quantity=100)

    # Negative price
    with pytest.raises(Exception):
        Product("MacBook Air M2", price=-10, quantity=100)

    # Negative quantity
    with pytest.raises(Exception):
        Product("MacBook Air M2", price=10, quantity=-100)

def test_prod_becomes_inactive():
    product = Product("MacBook Air M2", price=1450, quantity=100)

    product.set_quantity(0)

    assert product.get_quantity() == 0
    assert product.is_active() is False

def test_buy_modifies_quantity():
    product = Product("MacBook Air M2", price=1450, quantity=100)

    result = product.buy(2)

    assert product.get_quantity() == 98
    assert result == 2900

    product.buy(98)
    assert product.get_quantity() == 0
    assert product.is_active() is False

def test_buy_invalid_quantity():
    product = Product("MacBook Air M2", price=1450, quantity=100)

    with pytest.raises(Exception):
        product.buy(101)

    with pytest.raises(Exception):
        product.buy(0)

    with pytest.raises(Exception):
        product.buy(-1)
