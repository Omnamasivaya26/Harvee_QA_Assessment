from playwright.sync_api import Page, expect
from config.settings import BASE_URL, PASSWORD, STANDARD_USERNAME


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator('[data-test="error"]')

    def open(self):
        self.page.goto(BASE_URL, wait_until="domcontentloaded")

    def login(self, username=STANDARD_USERNAME, password=PASSWORD):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def expect_login_visible(self):
        expect(self.login_button).to_be_visible()
        expect(self.username_input).to_be_visible()

    def expect_error(self, message: str):
        expect(self.error_message).to_contain_text(message)
