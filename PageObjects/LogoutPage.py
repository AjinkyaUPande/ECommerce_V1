from selenium import webdriver
from selenium.webdriver.common.by import By


class Logout_Page:

    # Locators
    lnk_Logout_xpath = "//a[@class='ico-logout']"

    # Constructor

    def __init__(self, driver):
        self.driver = driver

    # Action Methods

    def ClickToLogout(self):
        self.driver.find_element(By.XPATH, self.lnk_Logout_xpath).click()