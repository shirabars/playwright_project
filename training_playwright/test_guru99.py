class TestGuru99:
    def test_guru99_login(self,setup_playwright):
        print ("into test_guru99_login")
        page = setup_playwright
        page.goto("https://demo.guru99.com/test/newtours/#google_vignette")
        user = page.locator("[name='userName']")
        user.fill("tutorial")
        password = page.locator("[name='password']")
        password.type("tutorial")
        submit = page.locator("[name='submit']")
        submit.click()

    def test_guru99_flight_search(self, setup_playwright):
        print("into test_guru99_flight_search")
        page = setup_playwright
        page.goto("https://demo.guru99.com/test/newtours/#google_vignette")

        page.get_by_role("link", name="Flights").click()

        page.locator("input[value='oneway']").click()
        passengers = page.locator("[name='passCount']")
        passengers.select_option("1")
        from_city = page.locator("[name='fromPort']")
        from_city.select_option("Paris")

        from_month = page.locator("[name='fromMonth']")
        from_month.select_option("January")
        from_day = page.locator("[name='fromDay']")
        from_day.select_option("1")

        to_port = page.locator("[name='toPort']")
        to_port.select_option("London")

        to_month = page.locator("[name='toMonth']")
        to_month.select_option("March")
        to_day = page.locator("[name='toDay']")
        to_day.select_option("1")

        servClass_radio_btn=page.locator("input[value='Business']")
        servClass_radio_btn.click()
        airline_dropdown=page.locator("[name='airline']")
        airline_dropdown.select_option("No Preference")

        continue_btn = page.locator("[name='findFlights']")
        continue_btn.click()

        print("test_flight_search_ is a success ")















        print("Flight search end")

