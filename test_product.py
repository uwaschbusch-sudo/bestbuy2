import pytest

from products import Product


def test_create_normal_product():
    """Prüft, dass ein normales Produkt angelegt wird."""
    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.get_quantity() == 100
    assert product.is_active() is True


def test_create_product_with_empty_name():
    """Prüft, dass ein leerer Name eine Ausnahme auslöst."""
    with pytest.raises(ValueError):
        Product("", price=1450, quantity=100)


def test_create_product_with_negative_price():
    """Prüft, dass ein negativer Preis eine Ausnahme auslöst."""
    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=-10, quantity=100)


def test_product_inactive_at_zero_quantity():
    """Prüft, dass ein Produkt bei Menge 0 inaktiv wird."""
    product = Product("MacBook Air M2", price=1450, quantity=1)
    product.set_quantity(0)
    assert product.is_active() is False


def test_buy_changes_quantity_and_returns_total_price():
    """Prüft, dass der Kauf die Menge ändert und den Gesamtpreis liefert."""
    product = Product("MacBook Air M2", price=1450, quantity=100)
    total_price = product.buy(10)
    assert total_price == 14500
    assert product.get_quantity() == 90


def test_buy_larger_quantity_than_stock():
    """Prüft, dass ein zu großer Kauf eine Ausnahme auslöst."""
    product = Product("MacBook Air M2", price=1450, quantity=100)
    with pytest.raises(ValueError):
        product.buy(101)