

class TestDemoblaze:
    def test_demoblaze_correct_login(self,setup_playwright):
        print ("into test_demoblaze_correct_login")
        page = setup_playwright
        page.goto("https://www.demoblaze.com/")

    def test_go_to_cart(self, setup_playwright):
        page = setup_playwright
        page.goto("https://www.demoblaze.com/")

    def test_add_product_to_cart(self, setup_playwright):
        page = setup_playwright
        page.goto("https://www.demoblaze.com/")
        cart_link = page.get_by_role("link", name="Cart")
        cart_link.click()
        current_url = page.url
        assert "cart.html" in current_url

