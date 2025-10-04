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

def test_case7(driver):
    Inventory_page = Inventory(driver)
    Inventory_page.open("https://www.saucedemo.com/")
    Inventory_page.add_cart(1)
    cart_badge = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//span[@class='shopping_cart_badge']"))
    )
    assert cart_badge.text == "1"
def test_case8(driver):
    Inventory_page = Inventory(driver)
    Inventory_page.open("https://www.saucedemo.com/")
    Inventory_page.add_cart(3)
    cart_badge = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//span[@class='shopping_cart_badge']"))
    )
    assert cart_badge.text == "3"

def test_case9(driver):
    Inventory_page = Inventory(driver)
    Inventory_page.open("https://www.saucedemo.com/")
    Inventory_page.remove_item_cart()
    cart_badge = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[@class='shopping_cart_link']"))
    )
    assert cart_badge.text == ""