import pytest
from pages.home_page import HomePage
from pages.common_actions import add_first_product_to_cart, go_to_cart
from pages.cart_page import CartPage

@pytest.mark.ui
def test_search_omega_and_add_to_cart(page, settings):
    # Шаги: открыть главную -> поиск «Омега» -> добавить первый товар -> перейти в корзину -> проверить позицию
    HomePage(page).open(settings["base_url"]).wait_loaded().search("Омега")
    add_first_product_to_cart(page)
    go_to_cart(page)
    CartPage(page).wait_loaded().should_have_items()
