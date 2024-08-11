from selenium import webdriver
import pytest


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome("./chromedriver.exe")

    pytest.driver.set_window_size(1400, 1000)

    pytest.driver.get('https://petfriends.skillfactory.ru/login')