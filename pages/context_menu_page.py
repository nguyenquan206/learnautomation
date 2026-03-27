from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ContextMenuPage(BasePage):
    CONTEXT_BOX = (By.ID, "hot-spot")

    def right_click_context_menu(self):
        self.right_click_element(self.CONTEXT_BOX)