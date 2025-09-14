# Централизованные селекторы с несколькими альтернативами (на случай изменений в верстке)
from typing import List

def any_of(*selectors: str) -> List[str]:
    return [s for s in selectors if s]

# Хедер/логотип/корзина
HEADER = any_of("header", "role=navigation", "[data-testid='header']")
LOGO = any_of("a[href='/' i] .logo", ".site-logo", "header a[aria-label*='UltraBalance' i]", "header a[href='/' i]")
CART_ICON = any_of("[href*='cart']", "a[aria-label*='корзина' i]", "a:has-text('Корзина')", "[data-testid='cart']")
CART_COUNT = any_of("[data-testid='cart-count']", ".cart-count", ".cart-badge")

# Поиск
SEARCH_INPUT = any_of("input[type=search]", "input[name=q]", "[placeholder*='Поиск' i]", "[data-testid='search']")
SEARCH_SUBMIT = any_of("[type=submit][value*='Поиск' i]", "button:has-text('Поиск')", "[data-testid='search-submit']")

# Карточка товара и покупка
PRODUCT_CARD = any_of("[data-testid='product-card']", ".product-card", ".catalog-card")
BUY_BUTTON = any_of("button:has-text('Купить')", "[data-testid='buy']", "button[aria-label*='Купить' i]")

# Корзина
CART_PAGE_ROOT = any_of("[data-testid='cart-page']", "[class*='cart']", "main:has-text('Корзина')")

# Статические страницы
FOOTER = any_of("footer", "[data-testid='footer']")
