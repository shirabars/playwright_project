import pytest
from playwright.sync_api import sync_playwright
from training_playwright.lululemon_project.pages.lulu_home_page import HomePage
import re

@pytest.fixture(scope="session")
def setup_playwright():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = context.new_page()
        yield page
        page.close()
        browser.close()

@pytest.fixture
def home(setup_playwright):
    page = setup_playwright
    page.goto("https://shop.lululemon.com/", wait_until="domcontentloaded")
    homeP = HomePage(page)
    homeP.close_popup()
    return homeP


@pytest.fixture
def sale_page(home):
    page = home.page
    sale_pattern = re.compile(r"Sale|Too Much", re.IGNORECASE)
    sale_link = page.locator("[data-testid='nav-desktop-l1']", has_text=sale_pattern)
    href = sale_link.get_attribute("href")
    full_url = f"https://shop.lululemon.com{href}"
    page.goto(full_url, wait_until="domcontentloaded")
    home.close_popup()
    page.wait_for_selector("h1", timeout=15000)
    from training_playwright.lululemon_project.pages.sale_page import SalePage
    return SalePage(page)

