

from playwright.sync_api import Page


class CheckoutcompletePO:
    def __init__(self,page:Page):
        self.page = page
        self.back_to_home_button = self.page.locator("//button[@id='back-to-products']")
        self.greetings_text = self.page.locator("//*[@id='checkout_complete_container']/h2")
        self.back_button = self.page.locator("//*[@id='back-to-products']")
        # self.back_to_home_button = self.page.evaluate("document.querySelectorAll('#back-to-products')")
        # self.color = self.page.evaluate('window.getComputedStyle(document.querySelector("")).getPropertyValue("property_name")')
