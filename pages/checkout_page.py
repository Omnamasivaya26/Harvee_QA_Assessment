from decimal import Decimal
from playwright.sync_api import Page, expect


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name = page.locator("#first-name")
        self.last_name = page.locator("#last-name")
        self.postal_code = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")
        self.cancel_button = page.locator("#cancel")
        self.error_message = page.locator('[data-test="error"]')
        self.subtotal_label = page.locator(".summary_subtotal_label")
        self.tax_label = page.locator(".summary_tax_label")
        self.total_label = page.locator(".summary_total_label")
        self.finish_button = page.locator("#finish")
        self.complete_header = page.locator(".complete-header")
        self.back_home_button = page.locator("#back-to-products")

    def expect_information_page(self):
        expect(self.page.locator(".title")).to_have_text("Checkout: Your Information")

    def expect_overview_page(self):
        expect(self.page.locator(".title")).to_have_text("Checkout: Overview")

    def enter_information(self, first_name, last_name, postal_code):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(postal_code)

    def continue_to_overview(self):
        self.continue_button.click()

    def expect_error(self, expected_text):
        expect(self.error_message).to_contain_text(expected_text)

    @staticmethod
    def _amount(text):
        return Decimal(text.split("$")[-1].strip())

    def get_subtotal(self):
        return self._amount(self.subtotal_label.inner_text())

    def get_tax(self):
        return self._amount(self.tax_label.inner_text())

    def get_total(self):
        return self._amount(self.total_label.inner_text())

    def finish_order(self):
        self.finish_button.click()
