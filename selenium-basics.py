from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "https://www.google.com/"
driver.get(url)

time.sleep(2)
driver.maximize_window()
driver.save_screenshot("screenshot.png")

url = "https://www.naver.com/"
driver.get(url)

print(driver.title)

time.sleep(2)

driver.back()
time.sleep(2)

driver.close()