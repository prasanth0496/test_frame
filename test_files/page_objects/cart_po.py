
class CartPO:
    def __init__(self,page):
        self.page = page
        self.checkout_button = self.page.locator("//*[@id='checkout']")