import re
from playwright.sync_api import expect

class SalePage:
    def __init__(self, page):
        self.page = page
        self.page_title = page.locator("h1")
        self.original_price = page.locator("span[class*='priceInactiveListPrice']")
        self.sale_price = page.locator("span[class*='price_price']").first

    def verify_on_sale_page(self):
        self.page.wait_for_url("**/we-made-too-much**", timeout=15000)
        h1 = self.page.locator("h1")
        expect(h1).to_have_text(re.compile(r"We Made Too Much", re.IGNORECASE), timeout=15000)
        return self

    def validate_discount_math(self):
        self.page.mouse.wheel(0, 500)
        self.original_price.first.wait_for(state="visible", timeout=15000)

        orig_text = self.original_price.first.inner_text()
        sale_text = self.sale_price.inner_text()

        orig_val = float(re.search(r'\d+', orig_text.replace(',', '')).group())
        sale_val = float(re.search(r'\d+', sale_text.replace(',', '')).group())

        print(f"DEBUG: Found Original: {orig_val}, Sale: {sale_val}")

        discount_pct = ((orig_val - sale_val) / orig_val) * 100
        assert discount_pct > 0, f"Error: Sale price {sale_val} is not lower than {orig_val}"

        return round(discount_pct, 2)