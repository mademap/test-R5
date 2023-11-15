from utilities.main import BaseDriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class Shopping(BaseDriver):

    def login(self):
        self.driver.find_element(By.ID, 'user-name').send_keys("standard_user")
        self.driver.find_element(By.ID, 'password').send_keys("secret_sauce")

    def click_button_login(self):
        self.driver.find_element(By.ID, 'login-button').click()

    def list_products(self):
        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
        self.driver.find_element(By.ID, 'shopping_cart_container').click()

    def confirm_product(self):
        self.driver.find_element(By.ID, 'checkout').click()

    def register_info(self):
        self.driver.find_element(By.ID, 'first-name').send_keys('Maria del Mar')
        self.driver.find_element(By.ID, 'last-name').send_keys('Polo Urriago')
        self.driver.find_element(By.ID, 'postal-code').send_keys('410001')
        self.driver.find_element(By.ID, 'continue').click()

    def finish_buy(self):
        self.driver.find_element(By.ID, 'finish').click()