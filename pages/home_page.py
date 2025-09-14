from playwright.sync_api import expect
from .base_page import BasePage, first_available
from . import selectors as S

class HomePage(BasePage):
    def wait_loaded(self):
        # Ждём хедер и футер как базовые элементы страницы
        first_available(self.page, S.HEADER)
        first_available(self.page, S.FOOTER)
        return self

    def title_should_contain_brand(self):
        expect(self.page).to_have_title(lambda t: "ultrabalance" in t.lower())
        return self

    def search(self, text: str):
        si = first_available(self.page, S.SEARCH_INPUT)
        si.fill(text)
        # Enter вместо кнопки — универсальней
        si.press("Enter")
        return self
