from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_home_page(self):
        self.driver.get(self.driver.current_url)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def wait_for_element_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def is_element_displayed(self, locator):
        try:
            self.wait_for_element_visible(locator)
            return True
        except:
            return False

    def click(self, locator):
        self.wait_for_element_visible(locator).click()

    def send_keys(self, locator, text):
        self.wait_for_element_visible(locator).send_keys(text)


