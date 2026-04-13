import time

from pages.home_page import HomePage
from pages.dynamic_content_page import DynamicContentPage

def test_dynamic_content(driver):
    driver.get("https://the-internet.herokuapp.com/")

    homepage = HomePage(driver)
    homepage.click_dynamic_content()

    dynamic_content = DynamicContentPage(driver)
    #Step 1: Get content
    content_1 = dynamic_content.get_content_text()
    #Step 2: Refresh page
    dynamic_content.refresh_page()
    #Step 3: Get content after refresh
    content_2 = dynamic_content.get_content_text()

    #Verify content is changed after refresh
    assert content_1 != content_2

def test_static_content(driver):
    driver.get("https://the-internet.herokuapp.com/dynamic_content?with_content=static")

    dynamic_content = DynamicContentPage(driver)
    # Step 1: Get content
    content_1 = dynamic_content.get_content_text()
    # Step 2: Refresh page
    dynamic_content.refresh_page()
    # Step 3: Get content after refresh
    content_2 = dynamic_content.get_content_text()

    # Verify content is NOT changed after refresh
    assert content_1 == content_2