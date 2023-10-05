
class CheckoutoverviewPO:
    def __init__(self,page):
        self.page = page
        self.finish_button = self.page.locator("//*[@id='finish']")