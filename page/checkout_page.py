from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CheckOut:
    def __init__(self , driver):
        self.driver = driver
    
    def open(self , url):
        self.driver.get(url)
        self.login()
        WebDriverWait(self.driver , 15).until(
            EC.element_to_be_clickable((By.XPATH , "/html/body/div/div/div/div[1]/div[1]/div[3]/a"))
        ).click()
        time.sleep(0.5)
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout"]'))
        ).click()
    
    def login(self):
        WebDriverWait(self.driver , 10).until(
            EC.visibility_of_element_located((By.ID , "user-name"))
        ).send_keys("standard_user")
        self.driver.find_element(By.ID , "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID , "login-button").click()
    def check_out(self , firstname , lastname , zipcode):
        wait = WebDriverWait(self.driver, 10)
        time.sleep(0.5)
        first_name_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='first-name']")))
        first_name_input.send_keys(firstname)
        time.sleep(0.5)
        last_name_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='last-name']")))
        last_name_input.send_keys(lastname)
        time.sleep(0.5)
        postal_code_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='postal-code']")))
        postal_code_input.send_keys(zipcode)
        time.sleep(0.5)
        continue_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='continue']")))
        continue_button.click()
        time.sleep(0.5)
        
        try:
            finish_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='finish']")))
            finish_button.click()
            time.sleep(0.5)
        except:
            pass
    def cancle(self , firstname , lastname , zipcode):
        wait = WebDriverWait(self.driver, 10)
        time.sleep(0.5)
        first_name_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='first-name']")))
        first_name_input.send_keys(firstname)
        time.sleep(0.5)
        last_name_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='last-name']")))
        last_name_input.send_keys(lastname)
        time.sleep(0.5)
        postal_code_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='postal-code']")))
        postal_code_input.send_keys(zipcode)
        time.sleep(0.5)
        continue_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='continue']")))
        continue_button.click()
        time.sleep(0.5)
        cancle_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='cancel']")))
        cancle_button.click()
        time.sleep(0.5)