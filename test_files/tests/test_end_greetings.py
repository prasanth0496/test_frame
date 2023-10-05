from library.cart_lib import CartLIB
from library.checkout_complete_lib import CheckoutcompleteLIB
from library.checkout_overview_lib import CheckoutoverviewLIB
from library.login_lib import LoginLIB
from library.products_lib import ProductsLIB
from library.user_details_lib import UserDetailsLIB


def test_end_greetings(page):
    login = LoginLIB(page)
    choose_products = ProductsLIB(page)
    cart = CartLIB(page)
    user_details = UserDetailsLIB(page)
    overview = CheckoutoverviewLIB(page)
    greetings = CheckoutcompleteLIB(page)
    page.goto("https://www.saucedemo.com/")
    login.login_to_app()
    choose_products.add_products()
    cart.checkout_cart()
    user_details.fill_user_details_at_checkout("ram","raj","5488")
    overview.process_overview()
    greetings.verify_text()







