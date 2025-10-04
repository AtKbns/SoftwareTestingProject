from selenium import webdriver

def create_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    return driver