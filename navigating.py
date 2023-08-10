from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

url = "https://github.com/" 
driver.get(url)

searchInput = driver.find_element(by=By.XPATH, value='//*[@id="query-builder-test"]')
time.sleep(1)

searchInput.send_keys("python")
time.sleep(2)
searchInput.send_keys(Keys.ENTER)
time.sleep(2)

results = driver.find_elements_by_css_selector(".results-list h3 a")

for element in results:
    print(element.text)
    
driver.close()
