from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains

class DragDropPage(BasePage):

    A_IMAGE = (By.ID, "column-a")
    B_IMAGE = (By.ID, "column-b")

    def drag_and_drop(self):
        source = self.wait_for_element_visible(self.A_IMAGE)
        target = self.wait_for_element_visible(self.B_IMAGE)

        actions = ActionChains(self.driver)
        actions.click_and_hold(source) \
            .move_to_element(target) \
            .release() \
            .perform()

    def is_swapped(self):
        source = self.wait_for_element_visible(self.A_IMAGE)
        target = self.wait_for_element_visible(self.B_IMAGE)

        return source.text == "B" and target.text == "A"