from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 6)

driver.get("https://ebay.com")
print('Loading Ebay webpage')
ebay_search_bar = wait.until(ec.element_to_be_clickable((By.XPATH, '//input[@id="gh-ac"]')))
print(f"The Webpage has been loaded. Current url is: {driver.current_url}")

my_search_input = "women watch"
print(f"Searching for \"{my_search_input}\"...")
ebay_search_bar.send_keys('women watch')
ebay_search_bar.send_keys(Keys.RETURN)

header = wait.until(ec.visibility_of_element_located((By.XPATH,
   "//h1[contains(@class, 'count-heading')]")))
ebay_header_text = header.text
print(f"Found in header: {ebay_header_text}")
assert f"results for {my_search_input}" in ebay_header_text
print('Test Passed. URL verified. The header “results for women watch“ present')
driver.quit()



#----output---
# Loading Ebay webpage
# The Webpage has been loaded. Current url is: https://www.ebay.com/
# Searching for "women watch"...
# Found in header: 590,000+ results for women watch
# Test Passed. URL verified. The header “results for women watch“ present
# 
# Process finished with exit code 0
