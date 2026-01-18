from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.ebay.com/")
    search=page.locator("//*[id='ge-ac']")
    search.type("shirt")
    search_button=page.locator("[id='gh-search-btn']")
    search_button.click()
    text=search_button.inner_text()
    # page.keyboard.press("Enter")
    print(page.title())

    page.close()
    browser.close()
    print("### Test end ###")

