from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):

    FORM_AUTH_LINK = (By.XPATH, "//a[text()='Form Authentication']")

    def click_form_auth(self):
        self.click(self.FORM_AUTH_LINK)