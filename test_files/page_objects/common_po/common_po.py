from playwright.sync_api import Page


class CommonPO:

    def __init__(self, page:Page):
        self.page = page
        self.hamburger = page.locator("//button[@id='react-burger-menu-btn']")



