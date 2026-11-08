import pytest
from config.settings import BASE_URL
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from tests.helpers import login_as_standard_user

@pytest.mark.order(22)
def test_TC22_products_page_is_not_accessible_after_logout(page):
    products = login_as_standard_user(page)
    products.logout()
    page.goto(f"{BASE_URL.rstrip('/')}/inventory.html", wait_until="domcontentloaded")
    LoginPage(page).expect_login_visible()
    assert "inventory.html" not in page.url
