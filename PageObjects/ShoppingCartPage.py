from selenium import webdriver
from selenium.webdriver.common.by import By


class ShoppingCart_Page:
    # Locators

    lnk_Computer_Xpath = "//a[contains(text(),'Computers')]"
    lnk_Desktop_Xpath = "(//a[normalize-space()='Desktops'])[3]"
    lnk_laptop_Xpath = "//h2[@class='product-title']//a[contains(text(),'Lenovo IdeaCentre 600 All-in-One PC')]"
    btn_AddToCart_Xpath = "//button[@class='button-1 add-to-cart-button']"
    lnk_ShoppingCart_Xpath = "//p[@class='content']//a[contains(text(),'shopping cart')]"
    cart_confirmation_Xpath = "//table[@class='cart']//a[contains(text(),'Lenovo IdeaCentre 600 All-in-One PC')]"

    # Constructor

    def __init__(self, driver):
        self.driver = driver

    # Action methods

    def ClickComputerLink(self):
        self.driver.find_element(By.XPATH, self.lnk_Computer_Xpath).click()

    def ClickDesktopLink(self):
        self.driver.find_element(By.XPATH, self.lnk_Desktop_Xpath).click()

    def ClickProductLink(self):
        self.driver.find_element(By.XPATH, self.lnk_laptop_Xpath).click()

    def ClickAddToCartBtn(self):
        self.driver.find_element(By.XPATH, self.btn_AddToCart_Xpath).click()

    def ClickShoppingCartLink(self):
        self.driver.find_element(By.XPATH, self.lnk_ShoppingCart_Xpath).click()

    def AddProductToCart(self):
        self.driver.find_element(By.XPATH, self.lnk_Computer_Xpath).click()
        self.driver.find_element(By.XPATH, self.lnk_Desktop_Xpath).click()
        self.driver.find_element(By.XPATH, self.lnk_laptop_Xpath).click()
        self.driver.find_element(By.XPATH, self.btn_AddToCart_Xpath).click()
        self.driver.find_element(By.XPATH, self.lnk_ShoppingCart_Xpath).click()

    def IsCartAdded(self):
        try:
            return self.driver.find_element(By.XPATH, self.cart_confirmation_Xpath).is_displayed()
        except:
            return False
