import pytest
from PageObjects.LoginPage import LoginPage
from PageObjects.RegistrationPage import Registration_Page
from PageObjects.ShoppingCartPage import ShoppingCart_Page
from PageObjects.OrderProduct import Order_Product
from time import sleep
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_006_LoginToCheckoutOptimized:
    baseURL = ReadConfig.getApplicationURL()
    user = ReadConfig.getUserMail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_CheckoutProduct(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(5)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        # Create the objects for respective page objects

        self.loginObj = LoginPage(self.driver)
        self.regObj = Registration_Page(self.driver)
        self.cartObj = ShoppingCart_Page(self.driver)
        self.checkoutObj = Order_Product(self.driver)

        # 1st Do registration
        self.logger.info("*** Started the Registration Process ***")
        self.regObj.ClickRegisterLink()
        self.regObj.AddRegistrationDetails('Mahesh', 'kumar', '10', 'October', '2009', self.user, 'CG', self.password)
        self.regObj.ClickRegisterBtn()

        # Then 2nd do login with that ID
        self.logger.info("*** Started the Login of Registered User ***")
        self.loginObj.ClickLogin()
        self.loginObj.LoginDetails(self.user, self.password)
        self.loginObj.ClickLoginBtn()

        # Then 3rd Add product to the cart

        self.logger.info("*** Selecting & Adding product to the cart ***")
        self.cartObj.AddProductToCart()

        # Then 4th checkout the product inside the cart

        self.logger.info("*** Started the checkout process ***")
        self.checkoutObj.AgreeTermsCheckbox()
        self.checkoutObj.ClickCheckoutBtn()
        self.checkoutObj.FillBillingAddress('India', 'Mumbai', 'Mumbai', '400401', '2365348777')
        self.checkoutObj.ClickBillingAddressContinueBtn()

        self.logger.info("*** Started completing necessary steps for checkout ***")
        self.checkoutObj.ContinueCheckoutByClicking()
        sleep(3)
        self.checkoutObj.ClickOrderConfirmation()
        self.logger.info("*** Order is Confirmed ***")

        self.expected = self.checkoutObj.IsOrderConfirmed()

        if self.expected:
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

        self.logger.info("*** End of test_006_LoginToCheckoutOptimized ***")
