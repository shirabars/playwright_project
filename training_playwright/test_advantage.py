


class TestAdvantage:
    def test_contact_us_btn(self, setup_playwright):
        print("into contact_us_btn")
        page = setup_playwright
        page.goto("https://advantageonlineshopping.com")
        page.wait_for_timeout(3000)
        contact_us_btn = page.get_by_role(role="link", name="CONTACT US")
        print(f"The text on the button is: {contact_us_btn.inner_text()}")
        contact_us_btn.click()

    def test_contactus_full_page(self, setup_playwright):
        page = setup_playwright
        page.goto("https://advantageonlineshopping.com/#/")
        page.wait_for_timeout(3000)
        page.get_by_text("CONTACT US").click()

        category_listbox = page.locator("[name='categoryListboxContactUs']")
        category_listbox.select_option(label="Speakers")

        product_select_listbox = page.locator("[name='productListboxContactUs']")
        product_select_listbox.select_option(label="Bose SoundLink Wireless Speaker")

        email_contact_us=page.locator("[name='emailContactUs']")
        email_contact_us.fill("demo@gmail.com")

        subject_text=page.locator("[name='subjectTextareaContactUs']")
        subject_text.fill("demo")

        send_btn = page.locator("#send_btn")
        send_btn.click()

        print("##test contact us page works good##")









