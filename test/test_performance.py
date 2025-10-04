import requests
import time
import threading
from page.inventory_page import Inventory
from utils.driver_factory import create_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page.checkout_page import CheckOut
def test_case16():
    start_time = time.time()
    requests.get("https://www.saucedemo.com/")
    end_time = time.time()

    elapsed_time = end_time - start_time

    assert elapsed_time <= 3

def test_case17():
    driver = create_driver()
    driver.get("https://www.saucedemo.com/")
    WebDriverWait(driver , 10).until(
            EC.visibility_of_element_located((By.ID , "user-name"))
        ).send_keys("standard_user")
    driver.find_element(By.ID , "password").send_keys("secret_sauce")
    start_time = time.time()
    driver.find_element(By.ID , "login-button").click()
    end_time = time.time()
    elapsed_time = end_time - start_time
    assert elapsed_time <= 5

def add():
    driver = create_driver()
    Inventory_page = Inventory(driver)
    Inventory_page.open("https://www.saucedemo.com/")
    start_time = time.time()
    Inventory_page.add_cart(1)
    end_time = time.time()
    elapsed_time = end_time - start_time
    assert elapsed_time <= 5
def test_case18():
    threads = []

    for _ in range(10):
        t = threading.Thread(target=add)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

def test_case19():
    driver = create_driver()
    start_time = time.time()
    checkout_page = CheckOut(driver)
    checkout_page.open("https://www.saucedemo.com/")
    checkout_page.check_out("Firstname" , "Lastname" , "Zipcode")
    end_time = time.time()
    elapsed_time = end_time - start_time
    assert elapsed_time <= 7

def check_get():
    start_time = time.time()
    requests.get("https://www.saucedemo.com/")
    elapsed_time = time.time() - start_time
    assert elapsed_time <= 25
def test_case20():
    threads = []

    for _ in range(10):
        t = threading.Thread(target=check_get)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    