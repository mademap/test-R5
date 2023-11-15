from selenium import webdriver
from selenium_testing_library import Screen
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os

load_dotenv()


class BaseDriver:
    def __init__(self):
        self.options = Options()
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--headless')
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--disable-blink-features=AutomationControlled')
        self.driver = webdriver.Chrome(options=self.options)
        self.browse_open()

    def browse_open(self):
        self.driver.get('https://www.saucedemo.com/')

    def closed_browser(self):
        self.driver.quit()
