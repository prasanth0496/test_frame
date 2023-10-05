from playwright.sync_api import Page


class LoginPO:
    def __init__(self, page: Page):
        self.page = page
        self.username_textbox = self.page.locator("//input[@id='user-name']")
        self.username_text = self.page.locator("//*[@id='login_credentials']")
        self.password_textbox = self.page.locator("//input[@id='password']")
        self.password_text = self.page.locator("//*[@id='root']/div/div[2]/div[2]/div/div[2]")
        self.login_button = self.page.locator("//input[@id='login-button']")
        self.error_message = self.page.locator("//*[@id='login_button_container']/div/form/div[3]/h3")
        # self.error_message = self.page.locator("//*[@id='login_button_container']/div/form/div[3]/h3")


