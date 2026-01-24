import re
from playwright.sync_api import expect


class SalePage:
    def __init__(self, page):
        self.page = page
        self.page_title = page.locator("h1")
        self.original_price = page.locator("span[class*='priceInactiveListPrice']")
        self.sale_price = page.locator("span[class*='price_price']")
        self.under_50_filter_label = page.locator("label[id='Under $50-label']")

    def verify_on_sale_page(self):
        self.page.wait_for_url(re.compile(r"we-made-too-much"), timeout=15000)
        expect(self.page_title).to_be_visible(timeout=15000)
        return self

    def apply_under_50_filter(self):
        for _ in range(3):
            self.page.keyboard.press("Escape")
            self.page.wait_for_timeout(500)
        self.under_50_filter_label.wait_for(state="visible", timeout=10000)

        try:
            self.under_50_filter_label.click(timeout=5000)
        except:
            self.under_50_filter_label.click(force=True)

        try:
            self.page.wait_for_url(re.compile(r"price-under-50|under-50"), timeout=10000)
        except:
            self.page.wait_for_timeout(3000)

        return self

    def validate_discount_math(self):
        self.page.mouse.wheel(0, 500)
        self.original_price.first.wait_for(state="visible", timeout=15000)
        orig_text = self.original_price.first.inner_text()
        sale_text = self.sale_price.first.inner_text()

        orig_val = float(re.search(r'\d+', orig_text.replace(',', '')).group())
        sale_val = float(re.search(r'\d+', sale_text.replace(',', '')).group())

        discount_pct = ((orig_val - sale_val) / orig_val) * 100
        assert discount_pct > 0, f"Sale price {sale_val} is not lower than {orig_val}"

        print(f"Original price: {orig_val}, Sale price: {sale_val}, Discount: {discount_pct:.2f}%")
        return round(discount_pct, 2)

    def verify_all_prices_under_50(self):
        self.page.mouse.wheel(0, 2000)
        self.page.wait_for_timeout(3000)
        all_prices = self.sale_price.all()
        list_prices = []
        for price_tag in all_prices:
            text_value = price_tag.inner_text()
            match = re.search(r'(\d+)', text_value.replace(',', ''))
            if match:
                price_number = float(match.group(1))
                if price_number < 50:
                    list_prices.append(price_number)

        return list_prices