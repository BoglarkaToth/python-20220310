from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# open browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://python.org")

# find go button
driver.find_element(By.ID, "id-search-field").send_keys("visual studio code")

# click button
driver.find_element(By.ID, "submit").click()

print("end")
