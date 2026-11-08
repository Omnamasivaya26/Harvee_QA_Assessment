import pytest
from pages.products_page import ProductsPage
from tests.helpers import login_as_standard_user

@pytest.mark.order(5)
def test_TC05_products_are_displayed_after_login(page):
    products = login_as_standard_user(page)
    assert products.product_cards.count() > 0
    assert products.product_names.count() == products.product_prices.count()
    assert products.product_images.count() == products.product_cards.count()
    assert products.add_buttons.count() == products.product_cards.count()
    assert all(name.strip() for name in products.get_names())
    assert all(price > 0 for price in products.get_prices())

@pytest.mark.order(6)
def test_TC06_sort_products_name_a_to_z(page):
    products = login_as_standard_user(page)
    products.sort("az")
    names = products.get_names()
    assert len(names) > 1
    assert names == sorted(names, key=str.casefold)

@pytest.mark.order(7)
def test_TC07_sort_products_name_z_to_a(page):
    products = login_as_standard_user(page)
    products.sort("za")
    names = products.get_names()
    assert len(names) > 1
    assert names == sorted(names, key=str.casefold, reverse=True)

@pytest.mark.order(8)
def test_TC08_sort_products_price_low_to_high(page):
    products = login_as_standard_user(page)
    products.sort("lohi")
    prices = products.get_prices()
    assert len(prices) > 1
    assert prices == sorted(prices)

@pytest.mark.order(9)
def test_TC09_sort_products_price_high_to_low(page):
    products = login_as_standard_user(page)
    products.sort("hilo")
    prices = products.get_prices()
    assert len(prices) > 1
    assert prices == sorted(prices, reverse=True)
