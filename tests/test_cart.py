import pytest
from playwright.sync_api import expect
from pages.cart_page import CartPage
from tests.helpers import login_as_standard_user

@pytest.mark.order(10)
def test_TC10_add_one_product_to_cart_updates_badge_and_button(page):
    products = login_as_standard_user(page)
    product = "Sauce Labs Backpack"
    products.add_product(product)
    products.expect_cart_badge(1)
    card = products.product_cards.filter(has_text=product)
    expect(card.get_by_role("button", name="Remove")).to_be_visible()

@pytest.mark.order(11)
def test_TC11_add_two_products_and_remove_one_in_cart(page):
    products = login_as_standard_user(page)
    products.add_product("Sauce Labs Backpack")
    products.add_product("Sauce Labs Bike Light")
    products.expect_cart_badge(2)
    products.open_cart()
    cart = CartPage(page)
    expect(cart.cart_items).to_have_count(2)
    cart.remove_product("Sauce Labs Bike Light")
    expect(cart.cart_items).to_have_count(1)
    assert cart.get_item_names() == ["Sauce Labs Backpack"]
    cart.expect_badge(1)

@pytest.mark.order(12)
def test_TC12_remove_product_from_products_page(page):
    products = login_as_standard_user(page)
    products.add_product("Sauce Labs Backpack")
    products.expect_cart_badge(1)
    products.remove_product("Sauce Labs Backpack")
    products.expect_cart_badge(0)

@pytest.mark.order(13)
def test_TC13_empty_cart_displays_no_products(page):
    products = login_as_standard_user(page)
    products.open_cart()
    cart = CartPage(page)
    cart.expect_empty()
    assert cart.get_item_names() == []

@pytest.mark.order(14)
def test_TC14_cart_details_match_selected_products(page):
    products = login_as_standard_user(page)
    products.add_product("Sauce Labs Backpack")
    products.add_product("Sauce Labs Bike Light")
    products.open_cart()
    cart = CartPage(page)
    assert set(cart.get_item_names()) == {"Sauce Labs Backpack", "Sauce Labs Bike Light"}
    assert len(cart.get_item_prices()) == 2
    assert all(price > 0 for price in cart.get_item_prices())
    expect(cart.item_quantities).to_have_count(2)
    assert cart.item_quantities.all_text_contents() == ["1", "1"]
