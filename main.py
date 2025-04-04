from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
stocks_links = []

#driver.get("https://google.com")
driver.get("https://investidor10.com.br/acoes/")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME,"actions"))
)

stocks_elements = driver.find_elements(By.CLASS_NAME,"actions")
#print(input_element)
for stock in stocks_elements: #get data from all pages
    try:
        title = stock.find_element(By.CLASS_NAME, "actions-title").text
        print(title)
        link_element = stock.find_element(By.TAG_NAME, "a")
        print(link_element.get_attribute("href"))
        stocks_links.append(link_element.get_attribute("href"))
    except:
        print("No title found in this action")


for stock in stocks_links:
    driver.get(stock)

#input_element.clear()
#input_element.send_keys("receba" + Keys.ENTER)
print()
print("end")
time.sleep(100)

driver.quit()
