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

# נאלצתי לשנות כמה פעמים כי היו שינויים בהצגת מבצעי האתר וחיפשתי משהו יציב יותר
@pytest.fixture
def sale_page(home):
    page = home.page
    women_nav = page.locator("a[data-testid='nav-desktop-l1']", has_text="Women")
    women_nav.hover()
    sale_link = page.locator("a[data-testid='features-list-item-9']", has_text="We Made Too Much")
    sale_link.click()
    from training_playwright.lululemon_project.pages.sale_page import SalePage
    return SalePage(page)