from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    # Locators
    lnk_login_xpath = "//a[@class='ico-login']"
    txt_email_xpath = "//input[@class='email']"
    txt_password_xpath = "//input[@name='Password']"
    btn_login_xpath = "//button[normalize-space()='Log in']"
    msg_confirmation_xpath = "//h2[normalize-space()='Welcome to our store']"

    # Constructor

    def __init__(self, driver):
        self.driver = driver

    # Action Methods

    def ClickLogin(self):
        self.driver.find_element(By.XPATH, self.lnk_login_xpath).click()

    def AddMail(self, mail):
        self.driver.find_element(By.XPATH, self.txt_email_xpath).send_keys(mail)

    def AddPass(self, password):
        self.driver.find_element(By.XPATH, self.txt_password_xpath).send_keys(password)

    def ClickLoginBtn(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

    def LoginDetails(self, email, password):
        self.driver.find_element(By.XPATH, self.txt_email_xpath).send_keys(email)
        self.driver.find_element(By.XPATH, self.txt_password_xpath).send_keys(password)

    def GetMsg(self):
        try:
            return self.driver.find_element(By.XPATH, self.msg_confirmation_xpath).is_displayed()
        except:
            return False
