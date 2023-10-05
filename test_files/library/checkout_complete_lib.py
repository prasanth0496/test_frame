from playwright.sync_api import expect, Page

from page_objects.checkout_complete_po import CheckoutcompletePO


class CheckoutcompleteLIB:
    def __init__(self, page:Page):
        self.page = page
        self.checkoutcomplete_po = CheckoutcompletePO(page)

    def complete_process(self):
        self.checkoutcomplete_po.back_to_home_button.click()

    def verify_text(self):
        text = self.checkoutcomplete_po.greetings_text.inner_text()
        assert "Thank you for your order!" == text

    def verify_back_button_color(self):
        expect(self.checkoutcomplete_po.back_button).to_have_css("color","rgb(19, 35, 34)")



