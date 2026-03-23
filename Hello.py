from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/")
time.sleep(5)
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("học automation")
time.sleep(5)
search_box.send_keys(Keys.RETURN)
time.sleep(10)

driver.quit()