"""
    Obect model for payment frame.
"""
from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit
import time
class Payment():
    
    PAYMENT_BUTTON=locators.PAYMENT_BUTTON
    iframe=locators.iframe
    email_id=locators.email_id
    card=locators.card
    expiry=locators.expiry
    cvc=locators.cvc
    zip_code=locators.zip_code
    submit=locators.submit
    payment_success=locators.payment_success
    
    #function to click on the payment button and switch frame
    @Wrapit._screenshot
    def go_to_payment(self):
        
        result_flag=self.click_payment_button()
        result_flag &=self.switch_frame(self.iframe)
        return result_flag
    
    #function to enter all the payment credentials 
    @Wrapit._screenshot
    def enter_payment_details(self):
        self.set_text(self.email_id,'akul@yahoo.com')
        self.set_text(self.card,'4242424242424242')
        self.set_text(self.expiry,'0224')
        self.set_text(self.cvc,'935')
        self.set_text(self.zip_code,'560039')
        self.click_element(self.submit)
        
    #function to check if the payment is successfull or not
    @Wrapit._screenshot
    def verify_success(self):
        result_flag=False
        if(self.get_text(self.payment_success).decode('utf-8')=='PAYMENT SUCCESS'):
            result_flag=True
        self.conditional_write(result_flag,
        positive="Payment done successfully",
        negative="Payment unsuccessfull")
        return result_flag
            
    #fuction call to click on the pay button
    def click_payment_button(self):
        result_flag=self.click_element(self.PAYMENT_BUTTON)
        return result_flag

