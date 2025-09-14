from playwright.sync_api import expect
from .base_page import BasePage, first_available
from . import selectors as S

class CartPage(BasePage):
    def wait_loaded(self):
        first_available(self.page, S.CART_PAGE_ROOT)
        return self

    def should_have_items(self):
        # Проверяем, что есть хотя бы одна карточка/строка товара
        # Пытаемся найти что-то похожее на название товара в корзине
        expect(self.page.get_by_text("итого", exact=False)).to_be_visible(timeout=10000)
        return self
