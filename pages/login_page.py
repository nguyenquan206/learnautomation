from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    USERNAME_TEXT = (By.ID, "username")
    PASSWORD_TEXT = (By.ID, "password")
    LOGGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    LOGOUT_BUTTON = (By.XPATH, "//a[@href='/logout']")
    LOGGIN_FAILED_TEXT = (By.XPATH, "//div[@id='flash' and contains(text(),'Your username is invalid!')]")

    def input_username(self, username):
        self.send_keys(self.USERNAME_TEXT, username)

    def input_password(self, password):
        self.send_keys(self.PASSWORD_TEXT, password)

    def click_login(self):
        self.click(self.LOGGIN_BUTTON)

    def is_logout_displayed(self):
        return self.is_element_displayed(self.LOGOUT_BUTTON)

    def is_loggin_fail_text_displayed(self):
        return self.is_element_displayed(self.LOGGIN_FAILED_TEXT)