from page_objects.checkout_overview_po import CheckoutoverviewPO


class CheckoutoverviewLIB:
    def __init__(self, page):
        self.page = page
        self.checkoutoverview_po = CheckoutoverviewPO(page)

    def process_overview(self):
        self.checkoutoverview_po.finish_button.click()
