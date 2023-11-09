from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#first test for check installation 

driver = webdriver.Chrome()
driver.get("http://www.ebay.com")
wait = WebDriverWait(driver, 5)
print(driver.current_url)
driver.close()

driver.quit()
