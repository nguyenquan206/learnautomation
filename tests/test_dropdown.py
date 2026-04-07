from pages.home_page import HomePage
from pages.dropdown_page import DropdownPage

def test_dropdown_page(driver):
    driver.get("https://the-internet.herokuapp.com/")

    homepage = HomePage(driver)
    homepage.click_dropdown_link()

    dropdown = DropdownPage(driver)
    #Select dropdown option 1
    print("Select Option 1")
    dropdown.select_option_by_value(1)
    assert dropdown.get_selected_option_text() == "Option 1"

    #Select dropdown option 2
    print("Select Option 2")
    dropdown.select_option_by_value(2)
    assert dropdown.get_selected_option_text() == "Option 2"