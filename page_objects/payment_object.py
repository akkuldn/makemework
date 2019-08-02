"""
    Obect model for payment frame.
"""
from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit
import time
class Payment():
    
    payment_button=locators.payment_button
    iframe=locators.iframe
    email_id=locators.email_id
    card=locators.card
    expiry=locators.expiry
    cvc=locators.cvc
    zip_code=locators.zip_code
    submit=locators.submit
    payment_success=locators.payment_success
    
    
    @Wrapit._screenshot
    def go_to_payment(self):
        "function to click on the payment button and switch frame"
        
        result_flag=self.click_payment_button()
        result_flag &=self.switch_frame(self.iframe)
        return result_flag
    
    @Wrapit._screenshot
    def enter_payment_details(self,email,card_no,expiry,cvc,zip_data):
        "function to enter all the payment credentials" 

        self.set_text(self.email_id,email)
        self.set_text(self.card,card_no)
        self.set_text(self.expiry,expiry)
        self.set_text(self.cvc,cvc)
        self.set_text(self.zip_code,zip_data)
        self.click_element(self.submit)
        
    @Wrapit._screenshot
    def verify_success(self,payment_success_msg):
        "function to check if the payment is successfull or not"
        result_flag=False
        if(self.get_text(self.payment_success).decode('utf-8')==payment_success_msg):
            result_flag=True
        self.conditional_write(result_flag,
        positive="Payment done successfully",
        negative="Payment unsuccessfull")
        return result_flag
            
    def click_payment_button(self):
        "fuction call to click on the pay button"

        result_flag=self.click_element(self.payment_button)
        return result_flag

