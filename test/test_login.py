import pytest
from page.login_page import LoginPage
from utils.driver_factory import create_driver

@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    driver.quit()

def test_case1(driver):
    login_page = LoginPage(driver)
    login_page.open("https://www.saucedemo.com/")
    login_page.login("standard_user" , "secret_sauce")
    driver.save_screenshot(f"images/tc1.png")
    assert "Swag Labs" in driver.title

def test_case2(driver):
    login_page = LoginPage(driver)
    login_page.open("https://www.saucedemo.com/")
    try:  
        login_page.login("standard_user" , "wrongpass")
        driver.save_screenshot(f"images/tc2.png")
        assert login_page.get_error() == "Epic sadface: Username and password do not match any user in this service"
    except AssertionError:
        raise

def test_case3(driver):
    login_page = LoginPage(driver)
    login_page.open("https://www.saucedemo.com/")
    try:  
        login_page.login("locked_out_user" , "secret_sauce")
        driver.save_screenshot(f"images/tc3.png")
        assert login_page.get_error() == "Epic sadface: Sorry, this user has been locked out."
    except AssertionError:
        raise

def test_case4(driver):
    login_page = LoginPage(driver)
    login_page.open("https://www.saucedemo.com/")
    try:  
        login_page.login("" , "secret_sauce")
        driver.save_screenshot(f"images/tc4.png")
        assert login_page.get_error() == "Epic sadface: Username is required"
    except AssertionError:
        raise

def test_case5(driver):
    login_page = LoginPage(driver)
    login_page.open("https://www.saucedemo.com/")
    try:  
        login_page.login("standard_user" , "")
        driver.save_screenshot(f"images/tc5.png")
        assert login_page.get_error() == "Epic sadface: Password is required"
    except AssertionError:
        raise

