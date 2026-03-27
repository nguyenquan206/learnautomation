from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):

    FORM_AUTH_LINK = (By.XPATH, "//a[text()='Form Authentication']")
    ADD_REMOVE_ELEMENT_LINK = (By.XPATH, '//a[contains(text(), "Add/Remove Elements")]')
    BASIC_AUTH_LINK = (By.XPATH, "//a[text()='Basic Auth']")
    CHECKBOXES_LINK = (By.XPATH, "//a[text()='Checkboxes']")
    CONTEXT_MENU_LINK = (By.XPATH, "//a[text()='Context Menu']")

    def click_form_auth(self):
        self.click(self.FORM_AUTH_LINK)

    def click_add_remove_element(self):
        self.click(self.ADD_REMOVE_ELEMENT_LINK)

    def click_basic_auth(self):
        self.click(self.BASIC_AUTH_LINK)

    def click_checkboxes(self):
        self.click(self.CHECKBOXES_LINK)

    def click_context_menu(self):
        self.click(self.CONTEXT_MENU_LINK)