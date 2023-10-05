from playwright.sync_api import expect

from library.cart_lib import CartLIB
from library.checkout_complete_lib import CheckoutcompleteLIB
from library.checkout_overview_lib import CheckoutoverviewLIB
from library.login_lib import LoginLIB
from library.products_lib import ProductsLIB
from library.user_details_lib import UserDetailsLIB


def test_button_color(page):
    login = LoginLIB(page)
    choose_products = ProductsLIB(page)
    cart = CartLIB(page)
    user_details = UserDetailsLIB(page)
    overview = CheckoutoverviewLIB(page)
    color = CheckoutcompleteLIB(page)
    page.goto("https://www.saucedemo.com/")
    login.login_to_app()
    choose_products.add_products()
    cart.checkout_cart()
    user_details.fill_user_details_at_checkout("ram","raj","5488")
    overview.process_overview()
    # button_color = page.get_by_text("Back Home")
    # a = page.locator("//*[@id='back-to-products']")
    # expect(a).to_have_css("color","rgb(19, 35, 34)")
    # expect(button_color).to_have_css("color","rgb(19, 35, 34)")
    color.verify_back_button_color()






