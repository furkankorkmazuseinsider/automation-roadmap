import unittest
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class LcwaikikiBasicSelenium(unittest.TestCase):
    TO_CATEGORY = (By.LINK_TEXT, "ERKEK")
    CATEGORY_PAGE = (By.CSS_SELECTOR, ".visible-md ")
    CATEGORY_TITLE = (By.TAG_NAME, "h3")
    SIZE_TITLE = (By.TAG_NAME, "h4")
    PRODUCT_PAGE = (By.CSS_SELECTOR, ".product-card__title ")
    CHOOSE_SIZE = (By.LINK_TEXT, "M")
    ADD_TO_CART = (By.ID, "pd_add_to_cart")
    ADD_TO_CART_BTN = (By.ID, "pd_add_to_cart")
    PAYMENT_STEP_BTN = (By.LINK_TEXT, "ÖDEME ADIMINA GEÇ")
    CART_PAGE = (By.ID, "shopping-cart")
    MAIN_PAGE = (By.CSS_SELECTOR, ".header__middle__left ")
    website = "https://www.lcwaikiki.com/tr-TR/TR"

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get(self.website)
        self.wait = WebDriverWait(self.driver, 15)

    def test_navigate(self):
        self.wait.until(ec.element_to_be_clickable(self.TO_CATEGORY)).click()
        self.assertTrue(self.wait.until(ec.element_to_be_clickable(self.CATEGORY_PAGE)))

        self.wait.until(ec.presence_of_all_elements_located(self.CATEGORY_PAGE))[4].click()
        self.assertIn("Tişört Ve Şortlar", self.wait.until(ec.presence_of_element_located(self.CATEGORY_TITLE)).text)

        self.wait.until(ec.presence_of_all_elements_located(self.PRODUCT_PAGE))[3].click()
        self.assertIn("Beden", self.wait.until(ec.presence_of_element_located(self.SIZE_TITLE)).text)
        time.sleep(4)

        self.wait.until(ec.element_to_be_clickable(self.CHOOSE_SIZE)).click()
        self.assertTrue(self.wait.until(ec.element_to_be_clickable(self.CHOOSE_SIZE)))

        self.wait.until(ec.element_to_be_clickable(self.ADD_TO_CART)).click()
        self.assertEqual("SEPETE EKLE", self.wait.until(ec.element_to_be_clickable(self.ADD_TO_CART_BTN)).text)

        self.wait.until(ec.element_to_be_clickable(self.CART_PAGE)).click()
        self.assertEqual("ÖDEME ADIMINA GEÇ", self.wait.until(ec.element_to_be_clickable(self.PAYMENT_STEP_BTN)).text)

        self.wait.until(ec.element_to_be_clickable(self.MAIN_PAGE)).click()
        self.assertTrue(self.wait.until(ec.element_to_be_clickable(self.MAIN_PAGE)))

    def tearDown(self):
        self.driver.quit()
