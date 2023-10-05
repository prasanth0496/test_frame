import logging

import pytest
from playwright.sync_api import expect

# from constants.constants import Constants
from library.login_lib import LoginLIB
from page_objects.login_po import LoginPO
from constants.constants import Constants




log_format = "%(asctime)s::%(levelname)s::%(name)s::"\
             "%(filename)s::%(lineno)d::%(message)s"
logging.basicConfig(filename='test_logs.log', level='DEBUG',  format=log_format)


def test_check_login_details(page):
    # logging.debug("Starting test_case_example...")
    login = LoginLIB(page)
    login_po = LoginPO(page)
    page.goto("https://www.saucedemo.com/")
    login.login_to_app("standard_user","hgdd")
    # logging.critical("test_case_example completed.")

    expect(login_po.error_message).to_contain_text(Constants.WRONG_PASSWORD_ERROR)
    # prsasnth

    # assert page.locator("//*[@id='login_button_container']/div/form/div[3]/h3").count()
    import sys
    print(sys.path)
