import time
import pytest
import os
from time import sleep
from PageObjects.LoginPage import LoginPage
from PageObjects.LogoutPage import Logout_Page
from utilities import XLUtils
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_003_LoginPage:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    path = r"C:\Users\apande\PycharmProjects\nopCommerce_V1\testData\nopCommerce_loginData.xlsx"

    # path = os.path.abspath(os.curdir) + "\\testData\\nopCommerce_loginData.xlsx"

    def test_LoginPageDDT(self, setup):
        self.logger.info("*** Starting the Test_003_LoginPage ***")

        self.rows = XLUtils.getRowCount(self.path, "Sheet1")
        lst_status = []

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.LoginPg = LoginPage(self.driver)
        self.LogoutPg = Logout_Page(self.driver)

        for r in range(2, self.rows + 1):
            self.LoginPg.ClickLogin()

            self.email = XLUtils.ReadData(self.path, "Sheet1", r, 1)
            self.password = XLUtils.ReadData(self.path, "Sheet1", r, 2)
            self.expected = XLUtils.ReadData(self.path, "Sheet1", r, 3)

            self.LoginPg.AddMail(self.email)
            self.LoginPg.AddPass(self.password)
            self.LoginPg.ClickLoginBtn()
            time.sleep(3)

            self.targetPage = self.LoginPg.GetMsg()

            if self.expected == 'Valid':
                if self.targetPage:
                    lst_status.append("Pass")
                    self.LogoutPg.ClickToLogout()
                else:
                    lst_status.append("Fail")
            elif self.expected == 'Invalid':
                if self.targetPage:
                    lst_status.append("Fail")
                    self.LogoutPg.ClickToLogout()
                else:
                    lst_status.append("Pass")

        self.driver.close()

        # Final Validation

        if "Fail" not in lst_status:
            assert True
        else:
            assert False
        self.logger.info("**** End of test_003_LoginPage_ddt ****")
