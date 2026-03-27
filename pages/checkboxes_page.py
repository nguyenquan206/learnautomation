from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class Checkboxes(BasePage):
    CHECKBOXES = (By.CSS_SELECTOR, "#checkboxes input")

    def get_checkboxes(self):
        return self.driver.find_elements(*self.CHECKBOXES)

    def tick_checkboxes_by_index(self, index):
        self.get_checkboxes()[index].click()

    def untick_checkboxes_by_index(self, index):
        self.get_checkboxes()[index].click()

    def is_checked_by_index(self, index):
        return self.get_checkboxes()[index].is_selected()