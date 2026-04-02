import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def create_driver(headless=False):
    options = Options()

    if headless:
        options.add_argument("--headless=new")

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver


@pytest.fixture
def driver():
    # Run on CI → enable headless
    is_ci = os.getenv("CI") == "true"

    driver = create_driver(headless=is_ci)

    yield driver

    driver.quit()