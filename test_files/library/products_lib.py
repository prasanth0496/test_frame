from page_objects.products_po import ProductsPO


class ProductsLIB:
    def __init__(self,page):
        self.page = page
        self.products_po = ProductsPO(page)

    def add_products(self):
        self.products_po.add_to_cart_button.click()
        self.products_po.container_button.click()
        self.products_po.hamburger.click()



