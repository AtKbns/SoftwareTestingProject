import pytest
from page.checkout_page import CheckOut
from utils.driver_factory import create_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    driver.quit()

def test_case9(driver):
    checkout_page = CheckOut(driver)
    checkout_page.open("https://www.saucedemo.com/")
    checkout_page.check_out("Firstname" , "Lastname" , "Zipcode")
    result = WebDriverWait(driver , 15).until(
        EC.visibility_of_element_located((By.XPATH , "//h2[normalize-space()='Thank you for your order!']"))
    ).text
    assert result == "Thank you for your order!"

def test_case10(driver):
    checkout_page = CheckOut(driver)
    checkout_page.open("https://www.saucedemo.com/")
    checkout_page.check_out("Firstname" , "Lastname" , "")
    result = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH , "//h3[normalize-space()='Error: Postal Code is required']"))
    ).text
    assert result == "Error: Postal Code is required"

def test_case11(driver):
    checkout_page = CheckOut(driver)
    checkout_page.open("https://www.saucedemo.com/")
    checkout_page.cancle("Firstname" , "Lastname" , "Zipcode")
    assert "Swag Labs" in driver.title
