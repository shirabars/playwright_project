from idna.codec import search_function
from playwright.sync_api import Page


class HomePage:

    def __init__(self, page):
        self.page = page
        self.search_input = "input.search-input"
        self.search_results = ".product-tile"

    def test_search_item(self, setup_playwright):
        page = setup_playwright
        page.goto("https://shop.lululemon.com")

        self.page.fill(self.search_input, setup_playwright)
        self.page.press(self.search_input, "Enter")

    def get_search_results(self, setup_playwright):
        page = setup_playwright
        page.goto("https://shop.lululemon.com")

        return self.page.query_selector_all(self.search_results)


    def count_search_results(self):
        return len(self.get_search_results())






