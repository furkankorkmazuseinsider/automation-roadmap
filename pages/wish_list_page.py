from pages.base_page import BasePage
from selenium.webdriver.common.by import By
#from pages.search_page import SearchPage


class WishListPage(BasePage):
    """Class is that including  functions about wish list page"""
    DELETE_BUTTON = (By.NAME, "submit.deleteItem")
    DELETED_TEXT = (By.XPATH, "//div[@class = 'a-alert-content' and text()='Deleted']")

    """def __init__(self, driver):
        self.search_page = SearchPage(driver)
        super().__init__(driver)"""

    def remove_product_in_wish_list(self):
        """Remove product from wish list"""

        self.click(*self.DELETE_BUTTON)

    def is_the_wish_list_empty(self):
        """Check wish list that is empty"""

        assert "Deleted" == self.visibility_element(self.DELETED_TEXT).text
