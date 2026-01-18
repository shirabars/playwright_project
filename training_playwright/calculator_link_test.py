import time
from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.calculator.net/")
    bmi_button =page.get_by_role(role="link",name="BMI Calculator")
    bmi_button.click()
    print(f"current_url is {page.url}")
    time.sleep(5)
    page.goto("https://www.calculator.net/")
    pace_button=page.get_by_role(role="link",name="Pace")
    pace_button.click()
    print(f"current_url is {page.url}")
    time.sleep(5)
    page.goto("https://www.calculator.net/")
    bmr_button=page.get_by_role(role="link",name="BMR")
    bmr_button.click()
    print(f"current_url is {page.url}")
    time.sleep(5)

    page.close()
    browser.close()
    print("### Test end ###")

