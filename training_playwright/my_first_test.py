from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    # user= page.locator("[id='user-name']")
    # user.fill("standard_user")
    # password=page.locator("[id='password']")
    # password.type("secret_sauce")
    current_url = page.url
    assert current_url == "https://www.saucedemo.com/", "current URL is not as expected""
    # print(f"current_url is {page.url}")
    page.close()
    browser.close()
    print("### Test end ###")


