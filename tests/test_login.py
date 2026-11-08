import pytest
from config.settings import BASE_URL, LOCKED_USERNAME, PASSWORD, STANDARD_USERNAME
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

@pytest.mark.order(1)
def test_TC01_standard_user_logs_in_successfully(page):
    login = LoginPage(page)
    login.open()
    login.login(STANDARD_USERNAME, PASSWORD)
    ProductsPage(page).expect_loaded()
    assert "/inventory.html" in page.url

@pytest.mark.order(2)
def test_TC02_locked_out_user_cannot_log_in(page):
    login = LoginPage(page)
    login.open()
    login.login(LOCKED_USERNAME, PASSWORD)
    login.expect_error("Sorry, this user has been locked out")
    assert "inventory.html" not in page.url

@pytest.mark.order(3)
def test_TC03_invalid_password_is_rejected(page):
    login = LoginPage(page)
    login.open()
    login.login(STANDARD_USERNAME, "wrong_password")
    login.expect_error("Username and password do not match")
    assert "inventory.html" not in page.url

@pytest.mark.order(4)
def test_TC04_empty_login_credentials_show_validation(page):
    login = LoginPage(page)
    login.open()
    login.login("", "")
    login.expect_error("Username is required")
    assert "inventory.html" not in page.url
