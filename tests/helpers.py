import pytest
from config.settings import BASE_URL, PASSWORD, STANDARD_USERNAME
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def login_as_standard_user(page):
    login = LoginPage(page)
    login.open()
    login.login(STANDARD_USERNAME, PASSWORD)
    products = ProductsPage(page)
    products.expect_loaded()
    return products


def start_checkout_with_products(page, products=None):
    products = products or ["Sauce Labs Backpack", "Sauce Labs Bike Light"]
    product_page = login_as_standard_user(page)
    for product in products:
        product_page.add_product(product)
    product_page.open_cart()
    cart = CartPage(page)
    cart.checkout()
    checkout = CheckoutPage(page)
    checkout.expect_information_page()
    return checkout
