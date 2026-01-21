import pytest
from playwright.sync_api import sync_playwright
from training_playwright.lululemon_project.pages.lulu_home_page import HomePage

@pytest.fixture(scope="session")
def setup_playwright(base_url):
    print (f"starting playwright into url {base_url} ")
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        page.close()
        browser.close()
        print("####Test end###")

@pytest.fixture
def home(setup_playwright):
    page = setup_playwright
    page.goto("https://shop.lululemon.com/story/women")
    home_obj = HomePage(page)
    home_obj.close_popup()
    return home_obj

# page = setup_playwright
# page.goto("https://shop.lululemon.com/story/women")
# home = HomePage(page) עטפתי את שלושת השורות האלו כאן כדי לנקות בטסטים

@pytest.fixture
def sale_page(home):
    page = home.page
    page.get_by_role("link", name="We Made Too Much", exact=True).first.click()
    page.wait_for_load_state("domcontentloaded")
    from training_playwright.lululemon_project.pages.sale_page import SalePage
    return SalePage(page)