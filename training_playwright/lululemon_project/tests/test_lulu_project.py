
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

def test_discount(sale_page):
    sale_page.verify_on_sale_page()
    discount = sale_page.validate_discount_math()

    assert discount >= 10, f"Expected at least 10% discount, but found {discount}%"

    print(f"*** The discount for the first item is {discount}% ***")

def test_validate_under_50_sale(sale_page):
    sale_page.verify_on_sale_page()
    sale_page.apply_under_50_filter()
    all_under_50_prices = sale_page.verify_all_prices_under_50()
    sorted_prices = sorted(all_under_50_prices)
    num_items = len(sorted_prices)

    print(f" Counted {len(sorted_prices)}under 50$ items.")
    if num_items > 0:
        print(f"Price Range: ${sorted_prices[0]} - ${sorted_prices[-1]}")

    assert num_items > 0, "No items were found in the Under $50 category"

    print(f"*** Tested 'Under $50' sale category. All {num_items} items are verified!")




