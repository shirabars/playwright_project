import time
from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.demoblaze.com/")
    log_in_btn = page.get_by_role(role="link", name="Log in")
    log_in_btn.click()
    user_name= page.locator("#loginusername")
    user_name.fill("tutorial")
    password= page.locator("#loginpassword")
    password.type("12345")
    login_submit_btn = page.get_by_role(role="button", name="Log in")
    login_submit_btn.click()
    print(f"current_url is {page.url}")
    page.close()
    browser.close()
    print("### Test end ###")

