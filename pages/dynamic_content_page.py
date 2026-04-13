from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DynamicContentPage(BasePage):
    CONTENT = (By.XPATH, "(//div[@class='large-10 columns'])[1]")

    def get_content_text(self):
        return self.wait_for_element_visible(self.CONTENT).text

    def refresh_page(self):
        self.driver.refresh()
