import pytest
from playwright.sync_api import expect
from constants.constants import Constants
# from file_utilities.json_file_handling_pandas import JsonFileHandling
from file_utilities.json_file_handling import JsonFileHandling
from library.login_lib import LoginLIB
from page_objects.login_po import LoginPO


def test_verify_login_jsonfile(page):
    login = LoginLIB(page)
    login_po = LoginPO(page)
    json_file = JsonFileHandling()
    login_details = json_file.read_file("C:\\Users\\Prasanth\\PycharmProjects\\Framework1\\file_utilities\\data.json")

    page.goto("https://www.saucedemo.com/")
    login.login_to_app(login_details["username"],login_details["password"])

    # expect(login_po.error_message).to_contain_text(Constants.WRONG_PASSWORD_ERROR)

    # assert page.locator("//*[@id='login_button_container']/div/form/div[3]/h3").count()
