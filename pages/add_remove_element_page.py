from random import random

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AddRemoveElementPage(BasePage):

    ADD_ELEMENT_BUTTON = (By.XPATH, '//button[contains(text(), "Add Element")]')
    DELETE_BUTTON = (By.XPATH, '//button[contains(text(), "Delete")]')

    def click_add_element(self):
        self.click(self.ADD_ELEMENT_BUTTON)

    def click_delete_element(self):
        self.click(self.DELETE_BUTTON)

    def click_add_multiple_elements(self, times):
        for i in range(times):
            if self.is_element_displayed(self.ADD_ELEMENT_BUTTON):
                self.click_add_element()
            else:
                break

    def click_delete_multiple_elements(self, times):
        for i in range(times):
            if self.is_element_displayed(self.DELETE_BUTTON):
                self.click_delete_element()
            else: break

    def count_delete_element_button(self):
        return len(self.driver.find_elements(*self.DELETE_BUTTON))