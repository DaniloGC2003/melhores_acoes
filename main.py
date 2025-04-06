from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import time
import csv

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
stocks_names = []
stocks_links = []
stocks_data = []

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
        #stocks_names.append(title)

        link_element = stock.find_element(By.TAG_NAME, "a")#get URL 
        print(link_element.get_attribute("href"))
        #stocks_links.append(link_element.get_attribute("href"))

        dict = {
            "name": title,
            "URL": link_element.get_attribute("href")
        }
        stocks_data.append(dict)
    except:
        print("No title found in this action")


with open("stocks_data.csv", 'w') as csv_output:
    csv_writer = csv.writer(csv_output, delimiter=",")
    fieldnames = ["company", "liquidity"]
    writer = csv.DictWriter(csv_output, fieldnames=fieldnames)
    writer.writeheader()


    for stock in stocks_data:#go through each URL and fill up .csv file
        #WebDriverWait(driver, 5).until(#idk
        #    EC.presence_of_element_located((By.ID, "table-indicators-company")),
        #    #EC.presence_of_element_located((By.CLASS_NAME,"cell"))
        #)
        liquidity = ""
        driver.get(stock["URL"])
        table_info = driver.find_element(By.ID, "table-indicators-company")
        info_arr = table_info.find_elements(By.CLASS_NAME, "cell")

        #find liquidity
        for cell in info_arr:
            if cell.find_element(By.CLASS_NAME, "title").text == "Liquidez Média Diária":
                liquidity_element = cell.find_element(By.CLASS_NAME, "value")
                liquidity_detailed = liquidity_element.find_element(By.CLASS_NAME, "detail-value")
                liquidity = liquidity_detailed.get_attribute("textContent").strip()
                print(liquidity)

        #find profits
        results_table = driver.find_element(By.ID, "results_table")
        results_table_values = results_table.find_element(By.NAME, "balance-results-values-view")
        results_table_values_select = Select(results_table_values)
        results_table_values_select.select_by_visible_text("Valores Detalhados")
        table_balance_results = results_table.find_element(By.ID,"table-balance-results")
        profit = table_balance_results.find_element(By.LINK_TEXT, "Lucro Bruto - (R$)")


        writer.writerow({"company": stock["name"], "liquidity": liquidity})
        pass



#with open("stocks_data.csv", 'w') as csv_output:
#    csv_writer = csv.writer(csv_output, delimiter=",")
    

#input_element.clear()
#input_element.send_keys("receba" + Keys.ENTER)
print()
print("end")
time.sleep(100)

driver.quit()
