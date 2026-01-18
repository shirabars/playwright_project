from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.guru99.com/test/newtours/#google_vignette")
    user= page.locator("[name='userName']")
    user.fill("tutorial")
    password=page.locator("[name='password']")
    password.type("tutorial")
    submit = page.locator("[name='submit']")
    submit.click()
    current_url = page.url
    print(f"current_url is {page.url}")
    page.close()
    browser.close()
    print("### Test end ###")