import pytest
from PageObjects.RegistrationPage import Registration_Page
import os
from time import sleep
from utilities import randomString
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_001_RegistrationPageNopCommerce:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    password = ReadConfig.getPassword()
    mail = randomString.RandomStringGenerator() + "@gmail.com"

    @pytest.mark.regression
    def test_RegistrationPage(self, setup):
        self.logger.info("*** test_001_RegistrationPageNopCommerce Started ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("*** Launching Application URL ***")
        self.driver.maximize_window()

        sleep(3)

        self.registration_Obj = Registration_Page(self.driver)

        self.logger.info("*** Clicking on registration link ***")

        self.registration_Obj.ClickRegisterLink()

        self.logger.info("*** Providing the customer details registration Details ***")

        self.registration_Obj.SelectGender()
        self.registration_Obj.AddFirstName("Kumar")
        self.registration_Obj.AddLastName("Mahesh")
        self.registration_Obj.DayOfBirth("1")
        self.registration_Obj.MonthOfBirth("October")
        self.registration_Obj.YearOfBirth("2009")
        self.registration_Obj.AddEmail(self.mail)
        # self.registration_Obj.AddEmail("MaheshKumar09@gmail.com")
        self.registration_Obj.AddCompanyName("IBM")
        # self.registration_Obj.SelectNewsletter()
        self.registration_Obj.CreatePassword(self.password)
        self.registration_Obj.ConfirmPassword(self.password)
        self.registration_Obj.ClickRegisterBtn()
        sleep(3)
        self.confMsg = self.registration_Obj.VerificationRegistration()
        sleep(3)
        if self.confMsg == "Your registration completed":
            assert True
            self.logger.info("*** Account Registration is Passed ***")
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_RegistrationPage.png")
            self.logger.error("*** Account registration is Failed ***")
            self.driver.close()
            assert False
        self.logger.info("*** test_001_RegistrationPageNopCommerce Finished ***")
