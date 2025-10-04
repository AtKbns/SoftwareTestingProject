import pytest
from page.inventory_page import Inventory
from utils.driver_factory import create_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    driver.quit()

def test_case12(driver):
    Inventory_page = Inventory(driver)
    Inventory_page.open("https://www.saucedemo.com/")
    Inventory_page.sort_item()
    prices = driver.find_elements(By.className , "inventory_item_price")
    price_list = []
    for price in prices:
        text = price.text 
        number = float(text.replace("$", "")) 
        price_list.append(number)
    assert price_list == sorted(price_list)

def test_case13(driver):
    Inventory_page = Inventory(driver)
    Inventory_page.open("https://www.saucedemo.com/") 
    Inventory_page.des_item()
    product_name = driver.find_element(By.XPATH , "//*[contain(text() , 'Sauce Labs Backpack')]")
    des_name = driver.find_element(By.XPATH , "//*[contain(text() , 'carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection.')]")
    price = driver.find_element(By.XPATH , "//*[contain(text() , '$29.99')]")
    assert product_name == "Sauce Labs Backpack" and des_name == "carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection." and price == "$29.99"


    