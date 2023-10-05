from page_objects.common_po.common_po import CommonPO


class ProductsPO(CommonPO):
    def __init__(self, page):
        CommonPO.__init__(self, page)
        # super(page)
        self.page = page
        self.add_to_cart_button = self.page.locator("//button[@id='add-to-cart-sauce-labs-backpack']")
        self.container_button = self.page.locator("//div[@id='shopping_cart_container']/a")
