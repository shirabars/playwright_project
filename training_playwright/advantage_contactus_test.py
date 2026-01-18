import time
from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://advantageonlineshopping.com/#/")
    time.sleep(10)
    contact_us_btn=page.get_by_role(role="link",name="CONTACT US")
    print(f"The text on the button is: {contact_us_btn.inner_text()}")
    contact_us_btn.click()
    time.sleep(3)

    page.close()
    browser.close()
    print("### Test end ###")

import pytest
class TestAdvantage:
    def test_advantage_shoping(self,setup_playwright):
        print("test_advantage_shoping")
        page = setup_playwright
        page.goto("https://advantageonlineshopping.com")
        time.sleep(10)

    def test_contactus_btn(self,setup_playwright):
        page = setup_playwright
        page.goto("https://advantageonlineshopping.com")
        time.sleep(10)
        page.get_by_text("CONTACT US").click()

    def test_categoryListbox(self, setup_playwright):
        page = setup_playwright
        page.goto("https://advantageonlineshopping.com/#/")
        time.sleep(10)
        page.get_by_text("CONTACT US").click()
        categoryListbox = page.locator("[name='categoryListboxContactUs']")
        categoryListbox.select_option(label="Speakers")



        print("Success: Speakers selected")