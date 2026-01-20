import time
from playwright.sync_api import expect
from training_playwright.lululemon_project.pages.lulu_home_page import HomePage



def test_search_item(setup_playwright):
    page = setup_playwright
    page.goto("https://shop.lululemon.com/story/women")

    page.keyboard.press("Escape")

    # search_bar = page.locator('[name="Ntt"]')
    search_input = page.locator("input[data-testid='nav-desktop-search']")
    search_input.fill("jacket")
    search_input.press("Enter")

    search_result = page.locator(".search-results_heading__QJ__C")
    expect(search_result).to_be_visible()

    print("*** test search results for jacket ***")

def test_feedback_button(setup_playwright):
    page = setup_playwright
    page.goto("https://shop.lululemon.com/story/women")




# def add_item_to_cart(page):
#     LoginPage(page).go_to()
#     LoginPage(page).login("standard_user", "secret_sauce")
#
#     home = HomePage(page)
#     home.add_first_product_to_cart()
#
#     cart = CartPage(page)
#     cart.open_cart()
#
#     assert cart.get_items_count() == 1
# 📄 utils/test_data.py