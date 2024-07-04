from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

gpu_prices_map = {}

options = webdriver.ChromeOptions()

options.add_argument('--headless')
# Uncomment/Comment the above line to turn headless mode on/off

driver = webdriver.Chrome(options=options)

driver.get("https://www.nvidia.com/en-in/geforce/buy/")

WebDriverWait(driver, 10).until(EC.title_contains("Shop GeForce RTX Series Graphics Cards and Desktops | NVIDIA"))
# Above line is used to wait for the title to show up i.e. waits for the page to fully load up to prevent any errors.

# Extracting the container element which contains the GPU names and prices
container = driver.find_elements(By.ID, "container-0c56a80eb9")

# Extracting the GPU names and prices
gpu_and_prices_elements = container[0].find_elements(By.CLASS_NAME, "title")

i = 0
while i < len(gpu_and_prices_elements):
    if i + 1 < len(gpu_and_prices_elements) and "Starting" in gpu_and_prices_elements[i+1].text: 
        # Checking if the price is available or not
        gpu_prices_map[gpu_and_prices_elements[i].text] = int(gpu_and_prices_elements[i+1].text[16:].replace(",", ""))
        i += 2 
    else:
        gpu_prices_map[gpu_and_prices_elements[i].text] = "N/A"
        i += 1

driver.quit()