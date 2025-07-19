from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

# pip3 install selenium
# pip3 install webdriver-manager
# to run this script , use "python3 hello world.py"
# Automatically downloads and sets up ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


driver.get("https://www.google.com")

#to interact with the search input field using its class name
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")

input_element.send_keys("Hello World" + Keys.RETURN)

time.sleep(5)  # Wait for results to load

driver.quit()  # Close the browser



