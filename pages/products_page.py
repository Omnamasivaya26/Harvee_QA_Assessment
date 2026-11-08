from decimal import Decimal
from playwright.sync_api import Page, expect


class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        self.page_title = page.locator(".title")
        self.sort_dropdown = page.locator('[data-test="product-sort-container"]')
        self.product_cards = page.locator(".inventory_item")
        self.product_names = page.locator(".inventory_item_name")
        self.product_prices = page.locator(".inventory_item_price")
        self.product_images = page.locator(".inventory_item_img img")
        self.add_buttons = page.get_by_role("button", name="Add to cart")
        self.cart_link = page.locator(".shopping_cart_link")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.menu_button = page.locator("#react-burger-menu-btn")
        self.logout_link = page.locator("#logout_sidebar_link")

    def expect_loaded(self):
        expect(self.page_title).to_have_text("Products")

    def sort(self, option: str):
        self.sort_dropdown.select_option(option)

    def get_names(self):
        return [v.strip() for v in self.product_names.all_text_contents()]

    def get_prices(self):
        return [Decimal(v.replace("$", "").strip()) for v in self.product_prices.all_text_contents()]

    def get_card_names(self):
        return self.get_names()

    def add_product(self, product_name: str):
        card = self.product_cards.filter(has_text=product_name)
        expect(card).to_have_count(1)
        card.get_by_role("button", name="Add to cart").click()

    def remove_product(self, product_name: str):
        card = self.product_cards.filter(has_text=product_name)
        expect(card).to_have_count(1)
        card.get_by_role("button", name="Remove").click()

    def open_cart(self):
        self.cart_link.click()

    def logout(self):
        self.menu_button.click()
        self.logout_link.click()

    def expect_cart_badge(self, expected_count: int):
        if expected_count == 0:
            expect(self.cart_badge).to_have_count(0)
        else:
            expect(self.cart_badge).to_have_text(str(expected_count))
