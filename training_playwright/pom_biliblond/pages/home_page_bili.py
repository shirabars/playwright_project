
class HomePageBili:

    def __init__(self, page):
        self.page = page

    def go_to(self):
        self.page.goto("https://biliblond.com/")

    def search_for_products(self, product_name: str):
        search = self.page.locator("input[name='q']")
        search.wait_for(state="visible", timeout=10000)
        search.fill(product_name)
        search.press("Enter")

    def get_results(self):
        return "search" in self.page.url.lower()

