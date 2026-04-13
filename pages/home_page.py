from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):

    FORM_AUTH_LINK = (By.XPATH, "//a[text()='Form Authentication']")
    ADD_REMOVE_ELEMENT_LINK = (By.XPATH, '//a[contains(text(), "Add/Remove Elements")]')
    BASIC_AUTH_LINK = (By.XPATH, "//a[text()='Basic Auth']")
    CHECKBOXES_LINK = (By.XPATH, "//a[text()='Checkboxes']")
    CONTEXT_MENU_LINK = (By.XPATH, "//a[text()='Context Menu']")
    DISAPPEAR_ELEMENT_LINK = (By.XPATH, "//a[text()='Disappearing Elements']")
    DRAG_DROP_LINK = (By.XPATH, "//a[text()='Drag and Drop']")
    DROPDOWN_LINK = (By.XPATH, "//a[text()='Dropdown']")
    DYNAMIC_CONTENT_LINK = (By.XPATH, "//a[text()='Dynamic Content']")

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

    def click_disappear_element(self):
        self.click(self.DISAPPEAR_ELEMENT_LINK)

    def click_drag_drop_link(self):
        self.click(self.DRAG_DROP_LINK)

    def click_dropdown_link(self):
        self.click(self.DROPDOWN_LINK)

    def click_dynamic_content(self):
        self.click(self.DYNAMIC_CONTENT_LINK)