from selenium import webdriver
from pages.home_page import HomePage
from pages.drag_drop_page import DragDropPage

def test_drag_drop(driver):
    driver.get("https://the-internet.herokuapp.com/")

    homepage = HomePage(driver)
    homepage.click_drag_drop_link()

    drag_drop_page = DragDropPage(driver)
    #Swap A with B
    drag_drop_page.drag_and_drop()

    #Verify after swap
    assert drag_drop_page.is_swapped()
