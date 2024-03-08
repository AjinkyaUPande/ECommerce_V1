from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


class Order_Product:
    # Locators
    checkbox_agreeTerms_xpath = "//input[@id='termsofservice']"
    button_checkout_xpath = "//button[@id='checkout']"
    txt_country_xpath = "//*[@id='BillingNewAddress_CountryId']"
    # txt_province_xpath = "//select[@id='BillingNewAddress_StateProvinceId']"  # Avoid(Faulty)
    txt_city_xpath = "//*[@id='BillingNewAddress_City']"
    txt_address_xpath = "//*[@id='BillingNewAddress_Address1']"
    txt_zipcode_xpath = "//*[@id='BillingNewAddress_ZipPostalCode']"
    txt_phoneNo_xpath = "//*[@id='BillingNewAddress_PhoneNumber']"
    continueBtn_billingAddr_xpath = "//button[@class='button-1 new-address-next-step-button']"
    radio_shippingType_xpath = "//input[@id='shippingoption_1']"
    continueBtn_ShippingMethod_xpath = "//button[@class='button-1 shipping-method-next-step-button']"
    radio_paymentMethod_xpath = "//input[@id='paymentmethod_0']"
    continueBtn_paymentMethod_xpath = "//button[@class='button-1 payment-method-next-step-button']"
    text_paymentInfo_xpath = "//p[contains(text(),'My Personal Check')]"
    continueBtn_paymentInfo_xpath = "//button[@class = 'button-1 payment-info-next-step-button']"
    productName_Confirmation_xpath = "//a[@class='product-name']"
    continueBtn_orderConfirmation_xpath = "//button[@class='button-1 confirm-order-next-step-button']"
    orderConfirmation_Msg_xpath = "//strong[contains(text(),'Your order has been successfully processed!')]"

    # Constructors
    def __init__(self, driver):
        self.driver = driver

    # Action methods

    def AgreeTermsCheckbox(self):
        self.driver.find_element(By.XPATH, self.checkbox_agreeTerms_xpath).click()

    def ClickCheckoutBtn(self):
        self.driver.find_element(By.XPATH, self.button_checkout_xpath).click()

    def AddCountry(self, nation):
        country = Select(self.driver.find_element(By.XPATH, self.txt_country_xpath))
        country.select_by_visible_text(nation)

    def AddCity(self, city):
        self.driver.find_element(By.XPATH, self.txt_city_xpath).send_keys(city)

    def AddShippingAddress(self, Address):
        self.driver.find_element(By.XPATH, self.txt_address_xpath).send_keys(Address)

    def AddZipcode(self, zipcode):
        self.driver.find_element(By.XPATH, self.txt_zipcode_xpath).send_keys(zipcode)

    def AddPhoneNo(self, phoneNo):
        self.driver.find_element(By.XPATH, self.txt_phoneNo_xpath).send_keys(phoneNo)

    def ClickBillingAddressContinueBtn(self):
        self.driver.find_element(By.XPATH, self.continueBtn_billingAddr_xpath).click()

    def SelectShippingTypeRadioBtn(self):
        self.driver.find_element(By.XPATH, self.radio_shippingType_xpath).click()

    def ClickShippingTypeContinueBtn(self):
        self.driver.find_element(By.XPATH, self.continueBtn_ShippingMethod_xpath).click()

    def SelectPaymentMethodRadioBtn(self):
        self.driver.find_element(By.XPATH, self.radio_paymentMethod_xpath).click()

    def ClickPaymentMethodContinueBtn(self):
        self.driver.find_element(By.XPATH, self.continueBtn_paymentMethod_xpath).click()

    def ClickPaymentInfoContinueBtn(self):
        self.driver.find_element(By.XPATH, self.continueBtn_paymentInfo_xpath).click()

    def FillBillingAddress(self, nation, city, addr, zipcode, phoneNo):
        country = Select(self.driver.find_element(By.XPATH, self.txt_country_xpath))
        country.select_by_visible_text(nation)
        self.driver.find_element(By.XPATH, self.txt_city_xpath).send_keys(city)
        self.driver.find_element(By.XPATH, self.txt_address_xpath).send_keys(addr)
        self.driver.find_element(By.XPATH, self.txt_zipcode_xpath).send_keys(zipcode)
        self.driver.find_element(By.XPATH, self.txt_phoneNo_xpath).send_keys(phoneNo)

    def ContinueCheckoutByClicking(self):
        self.driver.find_element(By.XPATH, self.radio_shippingType_xpath).click()
        self.driver.find_element(By.XPATH, self.continueBtn_ShippingMethod_xpath).click()
        self.driver.find_element(By.XPATH, self.radio_paymentMethod_xpath).click()
        self.driver.find_element(By.XPATH, self.continueBtn_paymentMethod_xpath).click()
        self.driver.find_element(By.XPATH, self.continueBtn_paymentInfo_xpath).click()

    def IsProductSame(self):
        productName = self.driver.find_element(By.XPATH, self.productName_Confirmation_xpath).getText()
        actual_name = "Lenovo IdeaCentre 600 All-in-One PC"
        if productName == actual_name:
            self.ClickOrderConfirmation()
            self.IsOrderConfirmed()
        else:
            assert False

    def ClickOrderConfirmation(self):
        self.driver.find_element(By.XPATH, self.continueBtn_orderConfirmation_xpath).click()

    def IsOrderConfirmed(self):
        try:
            return self.driver.find_element(By.XPATH, self.orderConfirmation_Msg_xpath).is_displayed()
        except:
            return False
