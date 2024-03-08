import pytest
from PageObjects.ShoppingCartPage import ShoppingCart_Page
from time import sleep
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from PageObjects.LoginPage import LoginPage


class Test_004_ShoppingCartPage:
    baseURL = ReadConfig.getApplicationURL()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    user = ReadConfig.getUserMail()

    def test_ShoppingCartPage(self, setup):
        self.logger.info("*** test_004_ShoppingCartPage Started ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(7)

        # Create Objects of related pages
        self.LogObj = LoginPage(self.driver)
        self.CartObj = ShoppingCart_Page(self.driver)

        self.logger.info("*** Clicking the Computer tab on navigation bar ***")
        self.CartObj.ClickComputerLink()

        sleep(2)
        self.logger.info("*** Clicking the Desktop tab under Computer tab ***")
        self.CartObj.ClickDesktopLink()

        sleep(2)
        self.logger.info("*** Selecting the product link ***")
        self.CartObj.ClickProductLink()

        sleep(4)
        self.logger.info("*** Adding selected product to the cart ***")
        self.CartObj.ClickAddToCartBtn()

        sleep(2)
        self.logger.info("*** Clicking shopping cart link to see the cart ***")
        self.CartObj.ClickShoppingCartLink()

        self.Expected = self.CartObj.IsCartAdded()

        if self.Expected:
            assert True
            self.driver.close()
            self.logger.info("*** The Test_004_ShoppingCartPage is Passed ***")
        else:
            self.logger.info("*** The Test_004_ShoppingCartPage is Failed ***")
            self.driver.close()
            assert False

        self.logger.info("*** End of test_004_ShoppingCartPage ***")
