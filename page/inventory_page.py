from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
class Inventory:
    def __init__(self , driver):
        self.driver = driver

    def open(self , url):
        self.driver.get(url)
        self.login()
    def login(self):
        WebDriverWait(self.driver , 10).until(
            EC.visibility_of_element_located((By.ID , "user-name"))
        ).send_keys("standard_user")
        self.driver.find_element(By.ID , "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID , "login-button").click()

    def add_cart(self , quantity):
        if quantity == 1:
            self.driver.find_element(By.ID , "add-to-cart-sauce-labs-backpack").click()
            time.sleep(3)
        if quantity == 3:
            WebDriverWait(self.driver , 10).until(
                EC.element_to_be_clickable((By.ID , "add-to-cart-sauce-labs-backpack"))
            ).click()
            time.sleep(3)
            WebDriverWait(self.driver , 15).until(
                EC.element_to_be_clickable((By.XPATH , "/html/body/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/button"))
            ).click()
            time.sleep(3)
            WebDriverWait(self.driver , 15).until(
                EC.element_to_be_clickable((By.XPATH , "/html/body/div/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/button"))
            ).click()
            time.sleep(3)
    
    def remove_item_cart(self):
        self.add_cart(3)
        self.driver.find_element(By.XPATH , "/html/body/div/div/div/div[1]/div[1]/div[3]/a").click()
        remove_btn = self.driver.find_elements(By.XPATH, "//button[text()='Remove']")
        for remove in remove_btn:
            time.sleep(2)
            remove.click()
    
    def sort_item(self):
        dropdown_element = self.driver.find_element(By.XPATH, "//select[@class='product_sort_container']")
        select = Select(dropdown_element)
        select.select_by_visible_text("Price (low to high)")
    
    def des_item(self):
        self.driver.find_element(By.XPATH , "//div[normalize-space()='Sauce Labs Backpack']").click()


