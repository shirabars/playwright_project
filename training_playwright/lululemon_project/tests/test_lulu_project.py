
from training_playwright.lululemon_project.pages.lulu_home_page import HomePage

def test_search_item(setup_playwright):
    page = setup_playwright
    page.goto("https://shop.lululemon.com/story/women")
    home = HomePage(page)

    home.close_popup()
    home.fill_search("jacket")
    home.press_search_enter()
    home.check_search_result_visible()

    print("*** test search results for jacket ***")


def test_search_invalid_product(setup_playwright):
    page = setup_playwright
    page.goto("https://shop.lululemon.com/story/women")
    home = HomePage(page)

    home.close_popup()
    home.fill_search("bitch")
    # סליחה על השפה אבל החיפוש רק לא מקבל קללות
    home.press_search_enter()
    home.verify_no_results_found()

    print("*** test search invalid input passed successfully ***")

def test_empty_bag_message(setup_playwright):
    page = setup_playwright
    page.goto("https://shop.lululemon.com")
    home = HomePage(page)

    home.close_popup()
    home.click_on_bag_icon()
    home.verify_bag_is_empty()

    print("*** test empty bag passed ***")


def test_feedback_button(setup_playwright):
    page = setup_playwright
    page.goto("https://shop.lululemon.com/story/women")
    page.keyboard.press("Escape")





