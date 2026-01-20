
from training_playwright.pom_biliblond.pages.home_page_bili import HomePageBili

def test_search_swimsuit(setup_playwright):
    page = setup_playwright
    home = HomePageBili(page)

    home.go_to()
    home.search_for_products("swimsuit")

    assert home.get_results(), "No search results found"
    print("*** test search results for swimsuit ***")







