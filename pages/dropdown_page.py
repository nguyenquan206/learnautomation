from selenium.webdriver.common.by import By
from pages.home_page import BasePage
from selenium.webdriver.support.ui import Select

class DropdownPage(BasePage):
    DROPDOWN_BOX = (By.XPATH, "//select[@id='dropdown']")

    def select_option_by_value(self, value):
        dropdown = Select(self.wait_for_element_visible(self.DROPDOWN_BOX))
        dropdown.select_by_value(str(value))

    def get_selected_option_text(self):
        dropdown = Select(self.wait_for_element_visible(self.DROPDOWN_BOX))
        return dropdown.first_selected_option.text