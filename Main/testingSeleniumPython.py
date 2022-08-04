from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pytest
import time

serv_obj = Service('Drive/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
def test_seleniumPython():
    driver.get("https://www.python.org/")
    driver.maximize_window()
    time.sleep(2)
    print(driver.title)
    python_logo = (driver.find_element(By.XPATH,"//*[@id='touchnav-wrapper']/header/div/h1/a/img"))
    print("display status:", python_logo.is_displayed())
    element = driver.find_element(By.XPATH,"//*[@id='id-search-field']")
    element.send_keys('python objects')
    driver.find_element(By.ID,"submit").click()
    print('********** seleniumPython test has passed *********************')
    assert True
    driver.close()

