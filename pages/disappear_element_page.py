from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait

class DisappearElementPage(BasePage):
    HOME_BUTTON = (By.XPATH, "//a[text() = 'Home']")
    ABOUT_BUTTON = (By.XPATH, "//a[text() = 'About']")
    CONTACT_US_BUTTON = (By.XPATH, "//a[text() = 'Contact Us']")
    PORTFOLIO_BUTTON = (By.XPATH, "//a[text() = 'Portfolio']")
    GALLERY_BUTTON = (By.XPATH, "//a[text() = 'Gallery']")

    def verify_disappearing_menu(self, base_url, timeout=10):
        menus = {
            "home": (self.HOME_BUTTON, base_url),
            "about": (self.ABOUT_BUTTON, "about"),
            "contact": (self.CONTACT_US_BUTTON, "contact"),
            "portfolio": (self.PORTFOLIO_BUTTON, "portfolio"),
            "gallery": (self.GALLERY_BUTTON, "gallery"),
        }

        for name, (locator, expected) in menus.items():
            if self.is_element_displayed(locator):
                print(f"{name} is displayed → testing...")

                self.click(locator)

                # wait URL change
                WebDriverWait(self.driver, timeout).until(
                    lambda d: expected in d.current_url.lower()
                )

                assert expected in self.driver.current_url.lower()

                self.driver.back()
            else:
                print(f"{name} is NOT displayed → skip")