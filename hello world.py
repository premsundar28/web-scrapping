from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


# Automatically downloads and sets up ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)




