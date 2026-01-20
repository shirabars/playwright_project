from playwright.sync_api import expect

from training_playwright.pom_swaglabs.pages.login_page import LoginPage


class TestLogin():


    def test_correct_login(self, setup_playwright):

        page = setup_playwright
        login_page = LoginPage(page)
        page.goto("https://www.saucedemo.com/")
        login_page.set_user_and_password()
        login_page.click_on_login()

        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
        assert page.url == "https://www.saucedemo.com/inventory.html","page URL is not as expected after login"

    def test_scc_login(self, setup_playwright):
        page = setup_playwright
        page.goto("https://www.saucedemo.com/")
        groups = page.query_selector_all(".form_group")

        groups[0].query_selector("input").fill("standard_user")
        groups[1].query_selector("input").fill("secret_sauce")

        page.click(".submit-button.btn_action")

        print("**test end**")
