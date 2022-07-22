from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    """Class is that including  functions about login page"""

    E_MAIL_ADRESS = "MAILADRESS"
    E_MAIL_PASSWORD = "PASSWORD"
    E_MAIL = (By.ID, "ap_email")
    E_MAIL_SUBMIT = (By.ID, "continue")
    PASSWORD = (By.ID, "ap_password")
    SIGN_IN_SUBMIT = (By.ID, "signInSubmit")

    def sign_in(self):
        """Fill and click login information"""

        self.fill(self.E_MAIL_ADRESS, *self.E_MAIL)
        self.click(*self.E_MAIL_SUBMIT)
        self.fill(self.E_MAIL_PASSWORD, *self.PASSWORD)
        self.click(*self.SIGN_IN_SUBMIT)
