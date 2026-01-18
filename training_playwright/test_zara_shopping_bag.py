class TestZara:

    def test_shopping_bag_text(self, setup_playwright):
        page = setup_playwright
        page.goto("https://www.zara.com/il/en/")

        shopping_bag_text = page.get_by_text("SHOPPING BAG").inner_text()
        assert shopping_bag_text == "SHOPPING BAG"
        print("##test shopping bag displayed by string##")

    def test_shopping_basket(self, setup_playwright):
        page = setup_playwright
        page.goto("https://www.zara.com/il/en/")

        basket=page.locator("[name='zds-empty-state__title']")
        if basket.count()==0:
            print("##shopping basket is empty##")
        else:
            print("##shopping basket is full##")
