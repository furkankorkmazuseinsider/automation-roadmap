from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    """Class is that including functions about homepage"""

    BASE_URL = "https://www.amazon.com/"
    SIGN_IN_BUTTON = (By.ID, "nav-link-accountList")
    DONT_CHANGE_BUTTON = (By.CSS_SELECTOR, ".a-button-inner:nth-child(1)")
    SEARCH_BOX = (By.ID, "twotabsearchtextbox")
    SEARCH_KEYWORD = "Samsung"
    SEARCH_BOX_BUTTON = (By.ID, "nav-search-submit-button")

    def go_to_sign_in(self):
        """Go to sign in site"""

        self.click(*self.DONT_CHANGE_BUTTON)
        self.click(*self.SIGN_IN_BUTTON)

    def search_keyword(self):
        """ Type and search word"""

        self.fill(self.SEARCH_KEYWORD, *self.SEARCH_BOX)
        self.click(*self.SEARCH_BOX_BUTTON)
