import pytest
from pages.home_page import HomePage

@pytest.mark.smoke
def test_homepage_is_up(page, settings):
    HomePage(page).open(settings["base_url"]).wait_loaded().title_should_contain_brand()

@pytest.mark.smoke
@pytest.mark.parametrize("path", ["/oferta", "/policy", "/return-policy"])
def test_static_pages_open(page, settings, path):
    HomePage(page).open(settings["base_url"] + path).wait_loaded()
