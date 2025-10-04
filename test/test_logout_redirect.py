import pytest
from page.login_page import LoginPage
from utils.driver_factory import create_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    driver.quit()


def test_case14(driver):
    login_page = LoginPage(driver)
    login_page.open("https://www.saucedemo.com/")
    login_page.login("standard_user" , "secret_sauce")
    login_page.logout()
    login_btn = driver.find_element(By.ID , "login-button")
    assert login_btn.get_attribute("value") == "Login"

def test_casee15(driver):
    driver.get("https://www.saucedemo.com/inventory.html")
    login_btn = driver.find_element(By.ID , "login-button")
    assert login_btn.get_attribute("value") == "Login"
