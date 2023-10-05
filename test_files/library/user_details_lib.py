from page_objects.user_details_po import UserdetailsPO


class UserDetailsLIB:
    def __init__(self,page):
        self.page = page
        self.userdetails_po = UserdetailsPO(page)

    def fill_user_details_at_checkout(self,firstname,lastname,pincode):
        self.userdetails_po.firstname_textbox.fill(firstname)
        self.userdetails_po.lastname_textbox.fill(lastname)
        self.userdetails_po.pincode_textbox.fill(pincode)
        self.userdetails_po.continue_button.click()




    # def finish_checkout(self,copoun=None):
    #     self.detail_po.container_button.click()
    #     self.detail_po.checkout_button.click()
    #
    #
    # def finish_checkout_with_copoun(self,copouncode):
    #     self.detail_po.container_button.click()
    #     self.detail_po.checkout_button.click()
    #     self.detail_po.checkout_button.click()
    #     self.detail_po.checkout_button.click()
    #     self.detail_po.checkout_button.click()
    #     self.detail_po.checkout_button.click()



