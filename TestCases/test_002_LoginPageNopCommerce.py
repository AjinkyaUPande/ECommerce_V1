import pytest
from PageObjects.LoginPage import LoginPage
import os
from time import sleep
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_002_LoginPageNopCommerce:
    baseURL = ReadConfig.getApplicationURL()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    user = ReadConfig.getUserMail()

    @pytest.mark.regression
    def test_loginPage(self, setup):
        self.logger.info("*** test_002_LoginPageNopCommerce Started ***")
        self.driver = setup
        self.logger.info("*** Launching Application URL ***")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        self.LogObj = LoginPage(self.driver)

        self.logger.info("*** Clicking on Login link ***")
        self.LogObj.ClickLogin()
        self.logger.info("*** Providing Customer Information ***")
        self.LogObj.AddMail(self.user)
        self.LogObj.AddPass(self.password)
        sleep(2)
        self.LogObj.ClickLoginBtn()
        sleep(3)

        self.targetPage = self.LogObj.GetMsg()
        if self.targetPage:
            assert True
            self.driver.close()
            self.logger.info("*** Account Login is Passed ***")
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_LoinPage.png")
            self.logger.info("*** Account Login is Failed ***")
            self.driver.close()
            assert False

        self.logger.info("*** End of test_002_login ***")
