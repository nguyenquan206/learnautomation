from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class BasicAuthPage(BasePage):
    LOGIN_SUCCESSFULLY_TEXT = (By.XPATH, "//p[contains(text(), 'Congratulations! You must have the proper credentials.')]")
    LOGIN_FAIL_TEXT = (By.XPATH, "//body[contains(text(), 'Not authorized')]")

    def is_logging_successful(self):
        return self.is_element_displayed(self.LOGIN_SUCCESSFULLY_TEXT)

    def is_logging_fail(self):
        return self.is_element_displayed(self.LOGIN_FAIL_TEXT)