
from playwright.sync_api import Page

from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.search_input = page.locator("input[data-testid='nav-desktop-search']")
        self.search_result = page.locator(".search-results_heading__QJ__C")
        self.no_results_title = page.locator("[class*='no-search-results_noTitleText']")
        self.bag_icon = page.locator("[data-testid='cart-icon']")
        self.empty_bag_title = page.locator("h1:has-text('Give your bag some love!')")
       #init של ההנחות
        self.women_nav = self.page.locator("a[data-testid='nav-desktop-l1']", has_text="Women")
        self.we_made_too_much_link = self.page.locator("a[data-testid='features-list-item-9']")

    def close_popup(self):
        self.page.keyboard.press("Escape")
        return self

    def fill_search(self, item_name: str):
        self.search_input.fill(item_name)
        return self

    def press_search_enter(self):
        self.search_input.press("Enter")
        return self

    def check_search_result_visible(self):
        expect(self.search_result).to_be_visible()
        return self

    def verify_no_results_found(self):
        expect(self.no_results_title).to_be_visible(timeout=10000)
        return self

    def click_on_bag_icon(self):
        self.bag_icon.click()
        return self

    def verify_bag_is_empty(self):
        expect(self.empty_bag_title).to_be_visible(timeout=7000)
        return self









