from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    """Class is that including  functions about product page"""

    ADD_TO_LIST_BUTTON = (By.ID, "add-to-wishlist-button-submit")
    WIEW_YOUR_LIST_BUTTON = (By.LINK_TEXT, "View Your List")

    def add_to_wish_list(self):
        """ Product is added to wish list"""

        self.click(*self.WIEW_YOUR_LIST_BUTTON)
