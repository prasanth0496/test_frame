
class UserdetailsPO:
    def __init__(self,page):
        self.page = page
        self.firstname_textbox = self.page.locator("//*[@id='first-name']")
        self.lastname_textbox = self.page.locator("//*[@id='last-name']")
        self.pincode_textbox = self.page.locator("//*[@id='postal-code']")
        self.continue_button = self.page.locator("//*[@id='continue']")


