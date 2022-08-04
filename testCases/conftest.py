import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
import selenium

@pytest.fixture
def setup(browser):
    if browser == "chrome":
        serv_obj = Service('Drive/chromedriver.exe')
        driver = webdriver.Chrome(service=serv_obj)
        print("Launching Chrome browser......................")
    elif browser == "firefox":
        serv_obj = Service('Drive/geckodriver.exe')
        driver = webdriver.Firefox(service=serv_obj)
        print("Launching Firefox browser......................")
    else:
        serv_obj = Service('Drive/msedgedriver.exe')
        driver = webdriver.Edge(service=serv_obj)
        print("Launching Edge browser.........................")

    return driver

def pytest_addoption(parser):            #This will get the value from CLI/Hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):     #This will return Browser value to setup method
    return request.config.getoption("--browser")

############################## Pytest HTML Report #############################################

#Hook for adding Environment info to HTML Report

def pytest_configure(config):
    config._metadata['Project Name'] = 'Swag Labs'
    config._metadata['Module Name'] = 'Login'
    config._metadata['Tester'] = 'Ade'

#Hook for delete/modify Environment info to HTML Report

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)