import pytest

from library.cart_lib import CartLIB
from library.checkout_complete_lib import CheckoutcompleteLIB
from library.checkout_overview_lib import CheckoutoverviewLIB
from library.login_lib import LoginLIB
from library.products_lib import ProductsLIB
from library.user_details_lib import UserDetailsLIB


@pytest.mark.fw
def test_frame(page):
    login_lib = LoginLIB(page)
    detail_lib = UserDetailsLIB(page)
    cart_lib = CartLIB(page)
    products_lib = ProductsLIB(page)
    checkout_complete_lib = CheckoutcompleteLIB(page)
    checkout_overview_lib = CheckoutoverviewLIB(page)
    page.goto("https://www.saucedemo.com/")
    login_lib.login_to_app("standard_user","secret_sauce")
    products_lib.add_products()
    cart_lib.checkout_cart()
    detail_lib.fill_user_details_at_checkout("prasanth","kumar","635109")
    # assert page.locator("//div[@id='checkout_summary_container']/div/div[2]/div[8]").count()
    checkout_overview_lib.process_overview()
    # assert page.locator("//div[@id='checkout_complete_container']/h2").count()
    checkout_complete_lib.complete_process()





