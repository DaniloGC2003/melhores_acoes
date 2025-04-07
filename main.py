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

current_page_stocks = "https://investidor10.com.br/acoes/"

get_next_URL = True
while get_next_URL:
    print("PÁGINA: ")
    print(current_page_stocks)
    driver.get(current_page_stocks)
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME,"actions"))
    )

    stocks_elements = driver.find_elements(By.CLASS_NAME,"actions")
    #print(input_element)
    for stock in stocks_elements: #get data from all pages
        try:
            title = stock.find_element(By.CLASS_NAME, "actions-title").text
            #print(title)
            #stocks_names.append(title)

            link_element = stock.find_element(By.TAG_NAME, "a")#get URL 
            #print(link_element.get_attribute("href"))
            #stocks_links.append(link_element.get_attribute("href"))

            dict = {
                "name": title,
                "URL": link_element.get_attribute("href")
            }
            stocks_data.append(dict)
        except:
            print("No title found in this action")
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME,"section-sectors-pagination"))
    )
    pagination_item_next = driver.find_element(By.CLASS_NAME, "section-sectors-pagination")
    #print(pagination_item_next.get_attribute("outerHTML"))
    #/html/body/div[3]/main/div[2]/section/div/div/div[5]
    #/html/body/div[3]/main/div[2]/section/div/div/div[5]/nav/ul/li[11]
    old_page_stocks = current_page_stocks
    current_page_stocks = pagination_item_next.find_element(By.XPATH, "./nav/ul/li[11]").find_element(By.CLASS_NAME, "pagination-link").get_attribute("href")
    if old_page_stocks == current_page_stocks or old_page_stocks + "#" == current_page_stocks:
        get_next_URL = False

    time.sleep(3)
    
    #pagination_item_next_link = pagination_item_next.find_element(By.CLASS_NAME, "pagination-link").get_attribute("href")
    #print(pagination_item_next_link)


with open("stocks_data.csv", 'w') as csv_output:
    csv_writer = csv.writer(csv_output, delimiter=",")
    fieldnames = ["company", "liquidity", "profit_last_year", "profit_2y", "profit_3y", "payout"]
    writer = csv.DictWriter(csv_output, fieldnames=fieldnames)
    writer.writeheader()


    for stock in stocks_data:#go through each URL and fill up .csv file
        #WebDriverWait(driver, 5).until(#idk
        #    EC.presence_of_element_located((By.ID, "table-indicators-company")),
        #    #EC.presence_of_element_located((By.CLASS_NAME,"cell"))
        #)

        liquidity = ""
        profit_last_year = ""
        profit_2y = ""
        profit_3y = ""
        payout = ""

        driver.get(stock["URL"])
        time.sleep(3)

        name_company = driver.find_element(By.CLASS_NAME, "name-company")
        print(name_company.get_attribute("textContent"))
        table_info = driver.find_element(By.ID, "table-indicators-company")
        info_arr = table_info.find_elements(By.CLASS_NAME, "cell")

        #find liquidity
        for cell in info_arr:
            if cell.find_element(By.CLASS_NAME, "title").text == "Liquidez Média Diária":
                liquidity_element = cell.find_element(By.CLASS_NAME, "value")
                liquidity_detailed = liquidity_element.find_element(By.CLASS_NAME, "detail-value")
                liquidity = liquidity_detailed.get_attribute("textContent").strip()
                print("liquidity: ", end='')
                print(liquidity)

        #find profits
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID,"results_table"))
        ) 
        results_table = driver.find_element(By.ID, "results_table")
        table_balance_results = results_table.find_element(By.ID,"table-balance-results")
        table_balance_results_tbody = table_balance_results.find_element(By.XPATH, "./*")
        table_balance_results_tbody_lines = table_balance_results_tbody.find_elements(By.XPATH, "./*")
        for item in table_balance_results_tbody_lines:
            values = item.find_elements(By.CLASS_NAME, "column-value")
            if (values[0].text == "Lucro Bruto - (R$)"):
                profit_last_year_el = values[2].find_element(By.CLASS_NAME, "detail-value")
                profit_last_year = profit_last_year_el.get_attribute("textContent")
                print("profit last year: ", end='')
                print(profit_last_year)

                profit_2y_el = values[3].find_element(By.CLASS_NAME, "detail-value")
                profit_2y = profit_2y_el.get_attribute("textContent")
                print("profit 2 years ago: ", end='')
                print(profit_2y)

                profit_3y_el = values[4].find_element(By.CLASS_NAME, "detail-value")
                profit_3y = profit_3y_el.get_attribute("textContent")
                print("profit 3 years ago: ", end='')
                print(profit_3y)

        #find payout
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID,"table-indicators-history"))
        )   
        table_indicators_history = driver.find_element(By.ID, "table-indicators-history")
        #print(table_indicators_history.get_attribute("outerHTML"))#maybe wait for table to load
        table_indicators_history_tbody = table_indicators_history.find_element(By.XPATH, "./*")
        table_indicators_history_tbody_lines = table_indicators_history_tbody.find_elements(By.XPATH, "./*")
        table_indicators_history_tbody_lines.pop(0)
        for item in table_indicators_history_tbody_lines:
            #print(item.get_attribute("outerHTML"))
            indicator = item.find_element(By.CLASS_NAME, "indicator")
            #print(indicator.get_attribute("textContent"))

            if "PAYOUT" in indicator.get_attribute("textContent"):
                #print("look at ya")
                payout_values = item.find_elements(By.CLASS_NAME, "value")
                payout = payout_values[0].get_attribute("textContent")
                print(payout)


        #remove "R$ " substring from liquidity
        liquidity = liquidity[3:]
        print(liquidity)
        writer.writerow({"company": stock["name"], 
                         "liquidity": liquidity, 
                         "profit_last_year": profit_last_year, 
                         "profit_2y": profit_2y, 
                         "profit_3y": profit_3y,
                         "payout": payout})
        pass



#with open("stocks_data.csv", 'w') as csv_output:
#    csv_writer = csv.writer(csv_output, delimiter=",")
    

#input_element.clear()
#input_element.send_keys("receba" + Keys.ENTER)
print()
print("end")
time.sleep(100)

driver.quit()
