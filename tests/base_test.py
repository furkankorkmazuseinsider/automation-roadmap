import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.home_page import HomePage


class BaseTest(unittest.TestCase):
    """Basic test cases"""

    def setUp(self):
        self.home_page_locators = HomePage
        option = Options()
        option.add_argument('--start-maximized')
        option.add_argument('--disable-notifications')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option)
        self.driver.implicitly_wait(10)
        self.driver.get(self.home_page_locators.BASE_URL)
