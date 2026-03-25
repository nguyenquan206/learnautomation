from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):

    FORM_AUTH_LINK = (By.XPATH, "//a[text()='Form Authentication']")
    ADD_REMOVE_ELEMENT_LINK = (By.XPATH, '//a[contains(text(), "Add/Remove Elements")]')

    def click_form_auth(self):
        self.click(self.FORM_AUTH_LINK)

    def click_add_remove_element(self):
        self.click(self.ADD_REMOVE_ELEMENT_LINK)