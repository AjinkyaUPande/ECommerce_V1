from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Registration_Page:

    # Locators
    lnk_registration_xpath = "//a[@class='ico-register']"
    radio_gender_xpath = "//input[@id='gender-male']"
    txt_firstname_xpath = "//input[@id='FirstName']"
    txt_lastname_xpath = "//input[@id='LastName']"
    txt_email_xpath = "//input[@id='Email']"
    txt_companyName_xpath = "//input[@id='Company']"
    chk_newsletter_xpath = "//input[@id='Newsletter']"
    txt_password_xpath = "//input[@name='Password']"
    txt_confirmPassword_xpath = "//input[@name='ConfirmPassword']"
    txt_date_xpath = "//*[@name='DateOfBirthDay']"
    txt_month_xpath = "//*[@name='DateOfBirthMonth']"
    txt_year_xpath = "//*[@name='DateOfBirthYear']"
    btn_register_xpath = "//button[contains(text(),'Register')]"  # //button[@id='register-button']
    txt_msg_confirm_xpath = "//*[contains(text(),'Your registration completed')]" #//*[@class="result"]

    # Constructor

    def __init__(self, driver):
        self.driver = driver

    # Action Methods

    def ClickRegisterLink(self):
        self.driver.find_element(By.XPATH, self.lnk_registration_xpath).click()

    def SelectGender(self):
        # Male selected
        self.driver.find_element(By.XPATH, self.radio_gender_xpath).click()

    def AddFirstName(self, firstname):
        self.driver.find_element(By.XPATH, self.txt_firstname_xpath).send_keys(firstname)

    def AddLastName(self, lastname):
        self.driver.find_element(By.XPATH, self.txt_lastname_xpath).send_keys(lastname)

    def DayOfBirth(self, inp_day):
        date = Select(self.driver.find_element(By.XPATH, self.txt_date_xpath))
        date.select_by_visible_text(inp_day)

    def MonthOfBirth(self, inp_month):
        month = Select(self.driver.find_element(By.XPATH, self.txt_month_xpath))
        month.select_by_visible_text(inp_month)

    def YearOfBirth(self, inp_year):
        year = Select(self.driver.find_element(By.XPATH, self.txt_year_xpath))
        year.select_by_visible_text(inp_year)

    def AddEmail(self, mail):
        self.driver.find_element(By.XPATH, self.txt_email_xpath).send_keys(mail)

    def AddCompanyName(self, company):
        self.driver.find_element(By.XPATH, self.txt_companyName_xpath).send_keys(company)

    def SelectNewsletter(self):
        self.driver.find_element(By.XPATH, self.chk_newsletter_xpath).click()

    def CreatePassword(self, password):
        self.driver.find_element(By.XPATH, self.txt_password_xpath).send_keys(password)

    def ConfirmPassword(self, confirm_pass):
        self.driver.find_element(By.XPATH, self.txt_confirmPassword_xpath).send_keys(confirm_pass)

    def ClickRegisterBtn(self):
        self.driver.find_element(By.XPATH, self.btn_register_xpath).click()

    def VerificationRegistration(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_msg_confirm_xpath).text
        except:
            None
