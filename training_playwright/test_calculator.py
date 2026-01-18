class TestCalculator:
    def test_select_interest_link(self,setup_playwright):
        page = setup_playwright
        page.goto("https://www.calculator.net/")
        interset=page.locator("[href='/interest-calculator.html']").click()
        interset.click()

    def test_interest_calculator_full(self, setup_playwright):
        page = setup_playwright
        page.goto("https://www.calculator.net/")
        page.locator("[href='/interest-calculator.html']").click()
        page.wait_for_load_state("networkidle")

        initial_investment=page.locator("[name='cstartingprinciple']")
        initial_investment.fill("10000")

        annual_contrib=page.locator("[name='cannualaddition']")
        annual_contrib.fill("5000")

        monthly_contrib=page.locator("[name='cmonthlyaddition']")
        monthly_contrib.fill("500")

        contribute_radio=page.get_by_role("radio", name="beginning")#("#cadditionat1")
        contribute_radio.check()

        interest_rate=page.locator("[name='cinterestrate']")
        interest_rate.fill("5")

        compound_dropdown=page.locator("[name='ccompound']")
        compound_dropdown.select_option(value="monthly")

        invest_years=page.locator("[name='cyear']")
        invest_years.fill("5")
        invest_months=page.locator("[name='cmonth']")
        invest_months.fill("0")

        tax_rate=page.locator("[name='ctaxtrate']")
        tax_rate.fill("0")

        inflation_rate=page.locator("[name='cinflationrate']")
        inflation_rate.fill("3")

        calc_btn = page.get_by_role("button", name="Calculate")
        calc_btn.click()

        financial_calculators = page.query_selector_all(".Financial.Calculators")
        print(financial_calculators)

        result_text=page.locator("div[class='verybigtext']").inner_text()
        print(f"Result text: {result_text}")

        assert "52000" in result_text, "Check result manually or adjust assert"














