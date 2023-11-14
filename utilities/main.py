from selenium import webdriver
from selenium_testing_library import Screen
from selenium.webdriver.chrome.options import Options


class BaseDriver:

    def _init_(self):
        self.options = Options()
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--headless')
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--disable-blink-features=AutomationControlled')
        self.driver = webdriver.Chrome(options=self.options)
        self.screen = Screen(self.driver)

    def browse_open(self):
        self.driver.get(URL)
        self.driver.delete_all_cookies()

    def closed_browser(self):
        self.driver.quit()

