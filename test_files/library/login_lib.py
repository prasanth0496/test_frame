from playwright.sync_api import Page

from page_objects.login_po import LoginPO


class LoginLIB:
    def __init__(self,page:Page):
        self.page = page
        self.login_po = LoginPO(page)

    def login_to_app(self,username=None,password=None):
        if username is None:
            username = self.login_po.username_text.inner_text().split('\n')[1]
            # self.login_po.get_username.inner_text().split('\n')[1]
        if password is None:
            password = self.login_po.password_text.inner_text().split('\n')[1]
        self.login_po.username_textbox.fill(username)
        self.login_po.password_textbox.fill(password)
        self.login_po.login_button.click()
        # return self.login_po.error_message


