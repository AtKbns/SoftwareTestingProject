from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self , driver):
        self.driver = driver
        self.username_input = (By.ID , "user-name")
        self.password_input = (By.ID , "password")
        self.btn_login = (By.ID , "login-button")
        self.error_msg = (By.CSS_SELECTOR , "h3[data-test='error']")
    
    def open(self , url):
        self.driver.get(url)
    
    def login(self , username , password):
        WebDriverWait(self.driver , 10).until(
            EC.visibility_of_element_located(self.username_input)
        ).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.btn_login).click()

    def get_error(self):
        try:
            return WebDriverWait(self.driver , 5).until(
                EC.visibility_of_element_located(self.error_msg)
            ).text
        except:
            return None
    
    def logout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))
        ).click()
        
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
        ).click()