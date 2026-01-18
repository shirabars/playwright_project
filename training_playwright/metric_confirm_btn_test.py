import time
from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.metric-conversions.org/")
    time.sleep(10)
    print(f"current_url is {page.url}")
    area_conversion_btn=page.get_by_role(role="link",name="Area conversion")
    if area_conversion_btn.is_visible():
        print("The button 'Area Conversion' text is correct")
    else:
        print("Could not find the correct text")
    area_conversion_btn.click()
    time.sleep(3)

    page.close()
    browser.close()
    print("### Test end ###")
