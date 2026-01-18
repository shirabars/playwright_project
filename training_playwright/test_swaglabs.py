
class TestSwaglabs:

    def test_swaglabs_correct_login(self,setup_playwright):
        print ("into test_swaglabs_correct_login")
        page = setup_playwright
        page.goto("https://www.saucedemo.com/")

        user = page.locator("#user-name")
        user.fill("standard_user")
        password = page.locator("#password")
        password.fill("secret_sauce")
        login_btn = page.get_by_text("login")
        login_btn.click()
        current_url = page.url
        assert current_url == "https://www.saucedemo.com/inventory.html", "current URL is not as expected"

    def test_swaglabs_incorrect_password_login(self, setup_playwright):
        print("into test_swaglabs_incorrect_login")
        page = setup_playwright
        page.goto("https://www.saucedemo.com/")

        user = page.locator("#user-name")
        user.fill("standard_user")
        password = page.locator("#password")
        password.fill("fake")
        login_btn = page.get_by_text("login")
        login_btn.click()
        current_url = page.url
        assert current_url == "https://www.saucedemo.com/", "current URL is not as expected"


    def test_swaglabs_incorrect_user_login(self, setup_playwright):
        print("into test_swaglabs_incorrect_login")
        page = setup_playwright
        page.goto("https://www.saucedemo.com/")
        user = page.locator("#user-name")
        user.fill("standard_user")
        password = page.locator("#password")
        password.fill("fake")
        login_btn = page.get_by_text("login")
        login_btn.click()
        current_url = page.url
        assert current_url == "https://www.saucedemo.com/", "current URL is not as expected"


    def test_swaglabs_get_first_price(self,setup_playwright):
        print ("into test_swaglabs_correct_login")
        page = setup_playwright
        page.goto("https://www.saucedemo.com/")

        user = page.locator("#user-name")
        user.fill("standard_user")
        password = page.locator("#password")
        password.fill("secret_sauce")
        login_btn = page.get_by_text("login")
        login_btn.click()
        list_prices = page.query_selector_all("[class='inventory_item_price']")
        first_price = list_prices[0]
        print (first_price.inner_text())

    def test_swaglabs_get_user_login_by_classes(self, setup_playwright):
        print("into test_swaglabs_correct_login_by_classes")
        page = setup_playwright
        page.goto("https://www.saucedemo.com/")
        


        print ("test end")
