from selenium import webdriver


options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=options)

url = "https://www.google.com"

driver.get(url)