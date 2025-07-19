from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome options
options = Options()
options.add_argument("--start-maximized")
# options.add_argument("--headless")  # You can enable this if needed

# Launch browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open Amazon search page
driver.get("https://www.amazon.in/s?k=iphone+15")

# Wait until search results are visible
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-component-type='s-search-result']")))

# Get top 10 products
products = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")[:10]

for i, product in enumerate(products, 1):
    try:
        title = product.find_element(By.XPATH, ".//h2//span").text
        price = product.find_element(By.XPATH, ".//span[@class='a-price']//span[@class='a-offscreen']").get_attribute("innerText")
        print(f"{i}. Product Name: {title}")
        print(f"   Price: {price}")
    except Exception as e:
        print(f"{i}. ❌ Error extracting data: {e}")

# driver.quit()
