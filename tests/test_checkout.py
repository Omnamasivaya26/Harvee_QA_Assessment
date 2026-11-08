import pytest
from decimal import Decimal
import pytest
from playwright.sync_api import expect
from config.settings import FIRST_NAME, LAST_NAME, POSTAL_CODE
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from tests.helpers import start_checkout_with_products

@pytest.mark.order(15)
def test_TC15_checkout_with_valid_information_reaches_overview(page):
    checkout = start_checkout_with_products(page, ["Sauce Labs Backpack"])
    checkout.enter_information(FIRST_NAME, LAST_NAME, POSTAL_CODE)
    checkout.continue_to_overview()
    checkout.expect_overview_page()
    expect(checkout.finish_button).to_be_visible()


@pytest.mark.parametrize(
    ("first_name", "last_name", "postal_code", "expected_error"),
    [
        ("", "Kumar", "642001", "First Name is required"),
        ("Manoj", "", "642001", "Last Name is required"),
        ("Manoj", "Kumar", "", "Postal Code is required"),
    ],
    ids=["missing-first-name", "missing-last-name", "missing-postal-code"],
)
@pytest.mark.order(16)
def test_TC16_TC17_TC18_checkout_required_field_validation(
    page, first_name, last_name, postal_code, expected_error
):
    checkout = start_checkout_with_products(page, ["Sauce Labs Backpack"])
    checkout.enter_information(first_name, last_name, postal_code)
    checkout.continue_to_overview()
    checkout.expect_error(expected_error)
    checkout.expect_information_page()

@pytest.mark.order(19)
def test_TC19_subtotal_tax_and_total_are_calculated_correctly(page):
    checkout = start_checkout_with_products(page, ["Sauce Labs Backpack", "Sauce Labs Bike Light"])
    checkout.enter_information(FIRST_NAME, LAST_NAME, POSTAL_CODE)
    checkout.continue_to_overview()
    checkout.expect_overview_page()
    subtotal = checkout.get_subtotal()
    tax = checkout.get_tax()
    total = checkout.get_total()
    assert subtotal == Decimal("39.98"), f"Unexpected subtotal: {subtotal}"
    assert total == subtotal + tax, f"Expected {subtotal} + {tax}, got {total}"

@pytest.mark.order(20)
def test_TC20_finish_order_shows_confirmation_and_empties_cart(page):
    checkout = start_checkout_with_products(page, ["Sauce Labs Backpack"])
    checkout.enter_information(FIRST_NAME, LAST_NAME, POSTAL_CODE)
    checkout.continue_to_overview()
    checkout.expect_overview_page()
    checkout.finish_order()
    expect(checkout.complete_header).to_contain_text("Thank you for your order")
    expect(checkout.back_home_button).to_be_visible()
    checkout.back_home_button.click()
    products = ProductsPage(page)
    products.expect_loaded()
    products.expect_cart_badge(0)
    products.open_cart()
    CartPage(page).expect_empty()

@pytest.mark.order(21)
def test_TC21_cancel_checkout_does_not_place_order_and_preserves_cart(page):
    checkout = start_checkout_with_products(page, ["Sauce Labs Backpack", "Sauce Labs Bike Light"])
    checkout.enter_information(FIRST_NAME, LAST_NAME, POSTAL_CODE)
    checkout.continue_to_overview()
    checkout.expect_overview_page()
    checkout.cancel_button.click()
    ProductsPage(page).expect_loaded()
    ProductsPage(page).expect_cart_badge(2)
    assert "checkout-complete" not in page.url
