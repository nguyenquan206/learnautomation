from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains

class HoverPage(BasePage):
    FIGURES = (By.CSS_SELECTOR, ".figure")
    USER_NAME = (By.CSS_SELECTOR, ".figcaption h5")

    def hover_on_user(self, index):
        figures = self.driver.find_elements(*self.FIGURES)
        ActionChains(self.driver).move_to_element(figures[index]).perform()

    def get_user_name(self, index):
        names = self.driver.find_elements(*self.USER_NAME)
        return names[index].text