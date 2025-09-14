import os
import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()

def _to_bool(val: str, default=True):
    if val is None:
        return default
    return val.strip().lower() in ("1","true","yes","y")

@pytest.fixture(scope="session")
def settings():
    return {
        "base_url": os.getenv("BASE_URL", "https://ultrabalance.ru"),
        "headless": _to_bool(os.getenv("HEADLESS","true"), True),
        "timeout_ms": int(os.getenv("TIMEOUT_MS","10000")),
    }

@pytest.fixture(scope="session")
def pw():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(pw, settings):
    browser = pw.chromium.launch(headless=settings["headless"])
    yield browser
    browser.close()

@pytest.fixture()
def context(browser):
    ctx = browser.new_context()
    yield ctx
    ctx.close()

@pytest.fixture()
def page(context, settings):
    p = context.new_page()
    p.set_default_timeout(settings["timeout_ms"])
    yield p
