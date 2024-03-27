import os

import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    current_directory = os.getcwd()
    options = webdriver.ChromeOptions()
    prefs = {"download.default_directory": current_directory[:-5]}
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
