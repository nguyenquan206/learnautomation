from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class BasicAuthPage(BasePage):
    LOGIN_SUCCESSFULLY_TEXT = (By.XPATH, "//p[contains(text(), 'Congratulations! You must have the proper credentials.')]")

    def is_logging_successful(self):
        return self.is_element_displayed(self.LOGIN_SUCCESSFULLY_TEXT)