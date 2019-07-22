#Common locator file for all locators
#Locators are ordered alphabetically

############################################
#Selectors we can use
#ID
#NAME
#css selector
#CLASS_NAME
#LINK_TEXT
#PARTIAL_LINK_TEXT
#XPATH
###########################################

#Locators for the Main page
TEMPERATURE_FIELD = "id,temperature"
BUY_BUTTON = "xpath,//button[contains(text(),'Buy %s')]"

#Product page
PAGE_HEADING = "xpath,//h2[text()='%s']"
PRODUCTS_LIST = "xpath,//div[contains(@class,'col-4')]"
ADD_PRODUCT_BUTTON = "xpath,//div[contains(@class,'col-4') and contains(.,'%s')]/descendant::button[text()='Add']"
CART_QUANTITY_TEXT = "id,cart"
CART_BUTTON = "xpath,//button[@onclick='goToCart()']"

#Cart page
CART_TITLE = "xpath,//h2[text()='Checkout']"
CART_ROW = "xpath,//tbody/descendant::tr"
CART_ROW_COLUMN = "xpath,//tbody/descendant::tr[%d]/descendant::td"
CART_TOTAL = "id,total"
PAYMENT_BUTTON="xpath,//span[text()='Pay with Card']"
iframe="//iframe[@name='stripe_checkout_app']"
email_id="xpath,//input[@placeholder='Email']"
card="xpath,//input[@placeholder='Card number']"
expiry="xpath,//input[@placeholder='MM / YY']"
cvc="xpath,//input[@placeholder='CVC']"
zip_code="xpath,//input[@placeholder='ZIP Code']"
submit="xpath,//button[@type='submit']"
payment_success="xpath,//h2"
