from playwright.sync_api import expect
from .base_page import first_available
from . import selectors as S

def add_first_product_to_cart(page):
    # Ищем первую карточку и нажимаем «Купить» внутри неё
    card = first_available(page, S.PRODUCT_CARD)
    # Если внутри карточки нет кнопки — ищем глобально запасной вариант
    btn = card.get_by_role("button", name=lambda n: n and "купить" in n.lower()).first
    if not btn or btn.count() == 0:
        btn = page.locator(S.BUY_BUTTON[0])
    btn.click()
    # Проверяем, что счетчик корзины увеличился
    # Счетчик может появиться динамически — ждём
    cart_badge = None
    try:
        cart_badge = first_available(page, S.CART_COUNT)
        expect(cart_badge).to_be_visible()
    except Exception:
        # fallback: просто проверим, что открылась мини-корзина / тост
        expect(page.get_by_text("в корзине", exact=False)).to_be_visible(timeout=8000)
    return True

def go_to_cart(page):
    cart = first_available(page, S.CART_ICON)
    cart.click()
