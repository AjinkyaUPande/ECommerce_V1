import os.path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from datetime import datetime


@pytest.fixture()
def setup(browser):
    if browser == 'edge':
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        driver.maximize_window()
        print("Launching Edge Browser...")
    elif browser == 'firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.maximize_window()
        print("Launching Firefox browser....")
    else:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        print("Launching Chrome Browser...")
    return driver


def pytest_addoption(parser):  # this will get the value from CLI/ hooks
    parser.addoption("--browser")


@pytest.fixture()  # Will return the browser value to the setup method
def browser(request):
    return request.config.getoption("--browser")


# ----------------------- Pytest Html Report Hooks ----------------------------


# This hook for adding environment info to the HTML report -> Not working
def pytest_configure(config):
    config._metadata = {
        'Project Name': 'nopCommerce',
        'Module Name': 'CustomerRegistration',
        "Tester": 'Ajinkya'
    }


# Its the hook to delete/ modify/ add Environment info to the Html report -> Working very fine
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata['Tester'] = 'Ajinkya'
    metadata['Project Name'] = 'nopCommerce'
    metadata['Module Name'] = 'CustomerRegistration'
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


# Specifying the report folder location & save report with the timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir) + "\\reports\\" + datetime.now().strftime(
        "%D-%M-%Y %H-%M-%S") + ".html"
