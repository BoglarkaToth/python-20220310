from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# open browser
def go_to_page():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:5500/docs/index.html")
    return driver
    
# find attribut
def get_text_of_paragraph(driver):
    content = driver.find_element(By.CSS_SELECTOR, ".important-p").text
    return content

driver = go_to_page()
content = get_text_of_paragraph(driver)

# print the att text
# print(content)
assert content == "This is th second paragraph."
# assert content == "xxx This is th second paragraph."

