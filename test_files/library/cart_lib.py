from page_objects.cart_po import CartPO


class CartLIB:
    def __init__(self,page):
        self.page = page
        self.cart_po = CartPO(page)

    def checkout_cart(self):
        self.cart_po.checkout_button.click()