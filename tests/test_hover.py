from pages.home_page import HomePage
from pages.hover_page import HoverPage

def test_hover_page(driver):
    driver.get("https://the-internet.herokuapp.com/hovers")

    hover = HoverPage(driver)

    for i in range(3):
        hover.hover_on_user(i)
        assert f"user{i + 1}" in hover.get_user_name(i)