import pytest
from PageObjects.LoginPage import LoginPage
from PageObjects.RegistrationPage import Registration_Page
from PageObjects.ShoppingCartPage import ShoppingCart_Page
from PageObjects.OrderProduct import Order_Product
from time import sleep
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_005_OrderProduct:
    baseURL = ReadConfig.getApplicationURL()
    user = ReadConfig.getUserMail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_OrderProduct(self, setup):
        # From login to the product order confirmation
        # Create the 3 objects related to Registration, login & then adding element to cart
        # then for order product object
        # this test is based on the known user & not using the ddt or dynamic data
        # to test on the application

        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.regObj = Registration_Page(self.driver)
        self.loginObj = LoginPage(self.driver)
        self.cartObj = ShoppingCart_Page(self.driver)
        self.orderObj = Order_Product(self.driver)

        # Start with Registration
        self.regObj.ClickRegisterLink()

        self.regObj.SelectGender()
        self.regObj.AddFirstName("Kumar")
        self.regObj.AddLastName("Mahesh")
        self.regObj.DayOfBirth("1")
        self.regObj.MonthOfBirth("October")
        self.regObj.YearOfBirth("2009")
        self.regObj.AddEmail(self.user)
        # self.registration_Obj.AddEmail("MaheshKumar09@gmail.com")
        self.regObj.AddCompanyName("IBM")
        # self.registration_Obj.SelectNewsletter()
        self.regObj.CreatePassword(self.password)
        self.regObj.ConfirmPassword(self.password)
        self.regObj.ClickRegisterBtn()

        # Start login from the same data

        self.logger.info("*** Clicking on Login link ***")
        self.loginObj.ClickLogin()
        self.logger.info("*** Providing Customer Information ***")
        self.loginObj.AddMail(self.user)
        self.loginObj.AddPass(self.password)
        sleep(2)
        self.loginObj.ClickLoginBtn()

        # Adding product to the cart

        self.cartObj.ClickComputerLink()
        sleep(2)
        self.cartObj.ClickDesktopLink()
        sleep(2)
        self.cartObj.ClickProductLink()
        sleep(4)
        self.cartObj.ClickAddToCartBtn()
        sleep(2)
        self.cartObj.ClickShoppingCartLink()

        # Checkout the products in cart

        self.orderObj.AgreeTermsCheckbox()
        self.orderObj.ClickCheckoutBtn()
        sleep(5)
        self.orderObj.AddCountry('India')
        sleep(5)
        self.orderObj.AddCity("Mumbai")
        sleep(5)
        self.orderObj.AddShippingAddress("Mumbai")
        sleep(3)
        self.orderObj.AddZipcode("400401")
        sleep(3)
        self.orderObj.AddPhoneNo("9912345672")
        sleep(2)
        self.orderObj.ClickBillingAddressContinueBtn()
        sleep(3)
        self.orderObj.SelectShippingTypeRadioBtn()
        sleep(3)
        self.orderObj.ClickShippingTypeContinueBtn()
        sleep(2)
        self.orderObj.SelectPaymentMethodRadioBtn()
        sleep(2)
        self.orderObj.ClickPaymentMethodContinueBtn()
        sleep(2)
        self.orderObj.ClickPaymentInfoContinueBtn()
        sleep(2)
        self.orderObj.ClickOrderConfirmation()
        sleep(2)
        self.expected = self.orderObj.IsOrderConfirmed()

        if self.expected:
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

        self.logger.info("*** End of test_005_OrderProduct ***")



