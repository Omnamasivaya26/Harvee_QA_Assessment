from decimal import Decimal
from playwright.sync_api import Page, expect


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_items = page.locator(".cart_item")
        self.item_names = page.locator(".cart_item .inventory_item_name")
        self.item_prices = page.locator(".cart_item .inventory_item_price")
        self.item_quantities = page.locator(".cart_quantity")
        self.checkout_button = page.locator("#checkout")
        self.continue_shopping_button = page.locator("#continue-shopping")
        self.cart_badge = page.locator(".shopping_cart_badge")

    def open(self):
        self.page.locator(".shopping_cart_link").click()

    def get_item_names(self):
        return [v.strip() for v in self.item_names.all_text_contents()]

    def get_item_prices(self):
        return [Decimal(v.replace("$", "").strip()) for v in self.item_prices.all_text_contents()]

    def remove_product(self, product_name: str):
        item = self.cart_items.filter(has_text=product_name)
        expect(item).to_have_count(1)
        item.get_by_role("button", name="Remove").click()

    def expect_badge(self, expected_count: int):
        if expected_count == 0:
            expect(self.cart_badge).to_have_count(0)
        else:
            expect(self.cart_badge).to_have_text(str(expected_count))

    def expect_empty(self):
        expect(self.cart_items).to_have_count(0)

    def checkout(self):
        self.checkout_button.click()
