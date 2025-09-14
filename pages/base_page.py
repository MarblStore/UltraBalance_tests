from typing import Iterable
from playwright.sync_api import Page, expect

def first_available(page: Page, selectors: Iterable[str]):
    last_error = None
    for sel in selectors:
        try:
            locator = page.locator(sel)
            expect(locator).to_be_visible(timeout=5000)
            return locator
        except Exception as e:
            last_error = e
    if last_error:
        raise last_error
    raise AssertionError("No selectors provided")

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str):
        self.page.goto(url, wait_until="domcontentloaded")
        return self

    def wait_visible(self, selector_or_loc):
        if isinstance(selector_or_loc, str):
            expect(self.page.locator(selector_or_loc)).to_be_visible()
        else:
            from playwright.sync_api import expect
            expect(selector_or_loc).to_be_visible()
        return self
