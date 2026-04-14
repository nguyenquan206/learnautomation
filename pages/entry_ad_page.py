from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class EntryAdPage(BasePage):
    MODAL = (By.ID, "modal")
    CLOSE_BUTTON = (By.XPATH, "//p[text()='Close']")
    REENABLE_LINK = (By.XPATH, "//a[text()='click here']")

    def is_modal_displayed(self):
        return self.wait_for_element_visible(self.MODAL)

    def is_modal_not_displayed(self):
        return WebDriverWait(self.driver, 5).until(
            EC.invisibility_of_element_located(self.MODAL)
        )

    def close_modal(self):
        element = self.wait_for_element_clickable(self.CLOSE_BUTTON)
        element.click()

    def refresh_page(self):
        self.driver.refresh()

    def click_reenable(self):
        element = self.wait_for_element_visible(self.REENABLE_LINK)
        element.click()

        WebDriverWait(self.driver, 5).until(
            lambda d: d.execute_script("return window.localStorage.getItem('seen')") is None
        )

    def wait_for_element_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )