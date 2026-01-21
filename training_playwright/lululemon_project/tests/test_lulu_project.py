
from training_playwright.lululemon_project.pages.lulu_home_page import HomePage

def test_search_item(home):
    home.fill_search("jacket")
    home.press_search_enter()
    home.check_search_result_visible()

    print("*** test search results for jacket ***")


def test_search_invalid_product(home):
    home.fill_search("bitch")
    # סליחה על השפה אבל החיפוש רק לא מקבל קללות
    home.press_search_enter()
    home.verify_no_results_found()

    print("*** test search invalid input passed successfully ***")

def test_empty_bag_message(home):
    home.click_on_bag_icon()
    home.verify_bag_is_empty()

    print("*** test empty bag passed ***")


def test_feedback_button(home):
    page = setup_playwright
    page.goto("https://shop.lululemon.com/story/women")
    page.keyboard.press("Escape")





