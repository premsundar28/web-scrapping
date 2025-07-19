from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open Amazon
driver.get("https://www.amazon.in/")
time.sleep(2)  # wait for page to load

# Find the search box and enter product name
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("iPhone 15")
search_box.send_keys(Keys.RETURN)

# Wait for results to load
time.sleep(3)

# (We'll extract price in the next step)
