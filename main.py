from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

import time
import csv


LIMIT_YEAR = 2020

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
stocks_names = []
stocks_links = []
stocks_data = []

current_page_stocks = "https://investidor10.com.br/acoes/"

#Find URLs for all stocks
get_next_URL = True
while get_next_URL:
    print("PÁGINA: ")
    print(current_page_stocks)
    driver.get(current_page_stocks)
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME,"actions"))
    )

    stocks_elements = driver.find_elements(By.CLASS_NAME,"actions")
    for stock in stocks_elements: #get data from all pages
        try:
            title = stock.find_element(By.CLASS_NAME, "actions-title").text

            link_element = stock.find_element(By.TAG_NAME, "a")#get URL 

            dict = {
                "name": title,
                "URL": link_element.get_attribute("href")
            }
            stocks_data.append(dict)
        except:
            print("No title found in this action")
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME,"section-sectors-pagination"))
    )
    pagination_item_next = driver.find_element(By.CLASS_NAME, "section-sectors-pagination")

    old_page_stocks = current_page_stocks
    current_page_stocks = pagination_item_next.find_element(By.XPATH, "./nav/ul/li[11]").find_element(By.CLASS_NAME, "pagination-link").get_attribute("href")
    if old_page_stocks == current_page_stocks or old_page_stocks + "#" == current_page_stocks or current_page_stocks == "https://investidor10.com.br/acoes/?page=9":
        get_next_URL = False


'''stocks_data = [{
                "name": "ITAUSA",
                "URL": "https://investidor10.com.br/acoes/itsa4/"
            }]'''

with open("stocks_data.csv", 'w') as csv_output:
    csv_writer = csv.writer(csv_output, delimiter=",")
    fieldnames = ["company", "current_price", "liquidity", "ev", "sector", "segment", 
                  "profit_last_year", "profit_2y", "profit_3y", "profit_4y", "profit_5y",
                  "ebit", "payout (%)", 
                  "divida_EBITDA", "divida_EBITDA_1y", "divida_EBITDA_2y", "divida_EBITDA_3y", "divida_EBITDA_4y", "divida_EBITDA_5y", 
                  "roe (%)", "roe_1y (%)", "roe_2y (%)", "roe_3y (%)", "roe_4y (%)", "roe_5y (%)",
                  "roic (%)", 
                  "vpa",
                  "lpa",
                  "pl", "pl_1y", "pl_2y", "pl_3y", "pl_4y", "pl_5y", 
                  "ev_ebit",
                  "cagr (%)", "cagr_1y (%)", "cagr_2y (%)", "cagr_3y (%)", "cagr_4y (%)", "cagr_5y (%)", 
                  "pvp", "pvp_1y", "pvp_2y", "pvp_3y", "pvp_4y", "pvp_5y", 
                  "dy (%)",]
    writer = csv.DictWriter(csv_output, fieldnames=fieldnames)
    writer.writeheader()


    for stock in stocks_data:#go through each URL and fill up .csv file
        skip_stock = False

        current_price = "-"
        liquidity = "-"
        ev = "-"
        sector = "-"
        segment = "-"
        profit_last_year = "-"
        profit_2y = "-"
        profit_3y = "-"
        profit_4y = "-"
        profit_5y = "-"
        ebit = "-"
        payout = "-"
        year_beginning = 0
        debt_EBITDA = '-'
        debt_EBITDA_1y = '-'
        debt_EBITDA_2y = '-'
        debt_EBITDA_3y = '-'
        debt_EBITDA_4y = '-'
        debt_EBITDA_5y = '-'
        roe = '-'
        roe_1y = '-'
        roe_2y = '-'
        roe_3y = '-'
        roe_4y = '-'
        roe_5y = '-'
        roic = '-'
        vpa = '-'
        lpa = '-'
        pl = '-'
        pl_1y = '-'
        pl_2y = '-'
        pl_3y = '-'
        pl_4y = '-'
        pl_5y = '-'
        ev_ebit = '-'
        cagr = '-'
        cagr_1y = '-'
        cagr_2y = '-'
        cagr_3y = '-'
        cagr_4y = '-'
        cagr_5y = '-'
        pvp = '-'
        pvp_1y = '-'
        pvp_2y = '-'
        pvp_3y = '-'
        pvp_4y = '-'
        pvp_5y = '-'
        dy = '-'

        driver.get(stock["URL"])


        try:
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.ID, "table-indicators-company"))
            )
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.CLASS_NAME, "name-company"))
            )
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.CLASS_NAME, "basic_info"))
            )
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.ID,"results_table"))
            ) 
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.ID,"table-indicators-history"))
            )
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.ID,"table-indicators"))
            )  
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.ID, "cards-ticker"))
            )  
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.ID, "info_about"))
            )  
        except TimeoutException:
            print("at least one element not found by the driver")
            skip_stock = True
        
        if not skip_stock:
            name_company = driver.find_element(By.CLASS_NAME, "name-company")
            print(name_company.get_attribute("textContent"))
            print(stock["URL"])
            table_info = driver.find_element(By.ID, "table-indicators-company")
            info_arr = table_info.find_elements(By.CLASS_NAME, "cell")

            basic_info = driver.find_element(By.CLASS_NAME, "basic_info")
            basic_info_table = basic_info.find_element(By.XPATH, "./*")
            basic_info_tbody = basic_info_table.find_element(By.XPATH, "./*")
            infos = basic_info_tbody.find_elements(By.XPATH, "./*")
            for item in infos:
                data = item.find_elements(By.XPATH, "./*")
                if data[0].get_attribute("textContent") == "Ano de estreia na bolsa:":
                    year_beginning = data[1].get_attribute("textContent")
                    if year_beginning == '':
                        year_beginning = 9999
                    else:
                        year_beginning = int(year_beginning)

                    print("estreia na bolsa: ", end='')
                    print(year_beginning)
                    

            #filter out companies before LIMIT_YEAR
            if year_beginning < LIMIT_YEAR:
                #find current price
                card_cotacao = driver.find_element(By.ID, "cards-ticker").find_elements(By.XPATH, "./*")[0]
                card_cotacao_body = card_cotacao.find_element(By.CLASS_NAME, "_card-body")
                current_price = card_cotacao_body.find_element(By.XPATH, "./div").get_attribute("textContent")
                if current_price != '-':
                    current_price = current_price.replace(',','.').replace(' ', '').replace('\n','')[2:]
                print('current price: ', end='')
                print(current_price)


                #find liquidity, EV, sector and segment
                for cell in info_arr:
                    if cell.find_element(By.CLASS_NAME, "title").text == "Liquidez Média Diária":
                        liquidity_element = cell.find_element(By.CLASS_NAME, "value")
                        liquidity_detailed = liquidity_element.find_element(By.CLASS_NAME, "detail-value")
                        liquidity = liquidity_detailed.get_attribute("textContent").strip()
                        #remove "R$ " substring from liquidity
                        liquidity = liquidity[3:].replace('.','')
                        print("liquidity: ", end='')
                        print(liquidity)
                    elif cell.find_element(By.CLASS_NAME, "title").text == "Setor":
                        sector_element = cell.find_element(By.CLASS_NAME, "value")
                        sector = sector_element.get_attribute("textContent").strip()
                        print("sector: ", end='')
                        print(sector)
                    elif cell.find_element(By.CLASS_NAME, "title").text == "Segmento":
                        segment_element = cell.find_element(By.CLASS_NAME, "value")
                        segment = segment_element.get_attribute("textContent").strip()
                        print("segment: ", end='')
                        print(segment)
                    elif cell.find_element(By.CLASS_NAME, "title").text == "Valor de firma":
                        ev_element = cell.find_element(By.CLASS_NAME, "value")
                        ev_detailed = ev_element.find_element(By.CLASS_NAME, "detail-value")
                        ev = ev_detailed.get_attribute("textContent").strip()
                        #remove "R$ " substring from EV
                        ev = ev[3:].replace('.','')
                        print("EV: ", end='')
                        print(ev)


                #find profits and EBIT
                results_table = driver.find_element(By.ID, "results_table")
                table_balance_results = results_table.find_element(By.ID,"table-balance-results")
                table_balance_results_tbody_list = table_balance_results.find_elements(By.XPATH, "./*")
                if table_balance_results_tbody_list:
                    table_balance_results_tbody = table_balance_results_tbody_list[0]
                    table_balance_results_tbody_lines = table_balance_results_tbody.find_elements(By.XPATH, "./*")
                    for item in table_balance_results_tbody_lines:
                        values = item.find_elements(By.CLASS_NAME, "column-value")
                        if (values[0].text == "Lucro Líquido - (R$)"):
                            profit_last_year_el = values[2].find_element(By.CLASS_NAME, "detail-value")
                            print(profit_last_year_el.get_attribute("textContent"))
                            profit_last_year = profit_last_year_el.get_attribute("textContent").replace('.','')
                            print("profit last year: ", end='')
                            print(profit_last_year)

                            profit_2y_el = values[3].find_element(By.CLASS_NAME, "detail-value")
                            profit_2y = profit_2y_el.get_attribute("textContent").replace('.','')
                            print("profit 2 years ago: ", end='')
                            print(profit_2y)

                            profit_3y_el = values[4].find_element(By.CLASS_NAME, "detail-value")
                            profit_3y = profit_3y_el.get_attribute("textContent").replace('.','')
                            print("profit 3 years ago: ", end='')
                            print(profit_3y)

                            '''profit_4y_el = values[5].find_element(By.CLASS_NAME, "detail-value")
                            profit_4y = profit_4y_el.get_attribute("textContent").replace('.','')
                            print("profit 4 years ago: ", end='')
                            print(profit_4y)

                            profit_5y_el = values[6].find_element(By.CLASS_NAME, "detail-value")
                            profit_5y = profit_5y_el.get_attribute("textContent").replace('.','')
                            print("profit 5 years ago: ", end='')'''
                            print(profit_5y)
                        elif (values[0].text == "EBIT - (R$)"):
                            ebit_el = values[1].find_element(By.CLASS_NAME, "detail-value")
                            ebit = ebit_el.get_attribute("textContent").replace('.','').replace("R$ ", "")
                            print("EBIT: ", end='')
                            print(ebit)

                else:
                    print ("no")


                #history indicators
                table_indicators_history = driver.find_element(By.ID, "table-indicators-history")
                try:
                    WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "basic_info"))
                    )
                    table_indicators_history_tbody = table_indicators_history.find_element(By.XPATH, "./*")
                    table_indicators_history_tbody_lines = table_indicators_history_tbody.find_elements(By.XPATH, "./*")
                    table_indicators_history_tbody_lines.pop(0)
                    for item in table_indicators_history_tbody_lines:
                        indicator = item.find_element(By.CLASS_NAME, "indicator")
                        if "P/L" in indicator.get_attribute("textContent"):
                            pl_values = item.find_elements(By.CLASS_NAME, "value")
                            try:
                                pl_1y = pl_values[1].get_attribute("textContent").replace('.','').replace(',','.')
                            except IndexError:
                                continue
                            try:
                                pl_2y = pl_values[2].get_attribute("textContent").replace('.','').replace(',','.')
                            except IndexError:
                                continue
                            try:
                                pl_3y = pl_values[3].get_attribute("textContent").replace('.','').replace(',','.')
                            except IndexError:
                                continue
                            '''try:
                                pl_4y = pl_values[4].get_attribute("textContent").replace('.','').replace(',','.')
                            except IndexError:
                                continue
                            try:
                                pl_5y = pl_values[5].get_attribute("textContent").replace('.','').replace(',','.')
                            except IndexError:
                                continue'''
                            print("P/L history: "  + pl_1y + ' ' + pl_2y + ' ' + pl_3y + ' ' + pl_4y + ' ' + pl_5y)
                        elif "P/VP" in indicator.get_attribute("textContent"):
                            pvp_values = item.find_elements(By.CLASS_NAME, "value")
                            try:
                                pvp_1y = pvp_values[1].get_attribute("textContent").replace('.','').replace(',','.')
                            except IndexError:
                                continue
                            try:
                                pvp_2y = pvp_values[2].get_attribute("textContent").replace('.','').replace(',','.')
                            except IndexError:
                                continue
                            try:
                                pvp_3y = pvp_values[3].get_attribute("textContent").replace('.','').replace(',','.')
                            except IndexError:
                                continue
                            ''' try:
                                pvp_4y = pvp_values[4].get_attribute("textContent").replace('.','').replace(',','.')
                            except IndexError:
                                continue
                            try:
                                pvp_5y = pvp_values[5].get_attribute("textContent").replace('.','').replace(',','.')
                            except IndexError:
                                continue'''
                            print("P/VP history: "  + pvp_1y + ' ' + pvp_2y + ' ' + pvp_3y + ' ' + pvp_4y + ' ' + pvp_5y)
                        elif "ROE" in indicator.get_attribute("textContent"):
                            roe_values = item.find_elements(By.CLASS_NAME, "value")
                            try:
                                roe_1y = roe_values[1].get_attribute("textContent").replace('.','').replace(',','.').replace('%','')
                            except IndexError:
                                continue
                            try:
                                roe_2y = roe_values[2].get_attribute("textContent").replace('.','').replace(',','.').replace('%','')
                            except IndexError:
                                continue
                            try:
                                roe_3y = roe_values[3].get_attribute("textContent").replace('.','').replace(',','.').replace('%','')
                            except IndexError:
                                continue
                            '''try:
                                roe_4y = roe_values[4].get_attribute("textContent").replace('.','').replace(',','.').replace('%','')
                            except IndexError:
                                continue
                            try:
                                roe_5y = roe_values[5].get_attribute("textContent").replace('.','').replace(',','.').replace('%','')
                            except IndexError:
                                continue'''
                            print("ROE history: "  + roe_1y + ' ' + roe_2y + ' ' + roe_3y + ' ' + roe_4y + ' ' + roe_5y)
                        elif "DÍVIDA LÍQUIDA / EBITDA" in indicator.get_attribute("textContent"):
                            debt_EBITDA_values = item.find_elements(By.CLASS_NAME, "value")
                            try:
                                debt_EBITDA_1y = debt_EBITDA_values[1].get_attribute("textContent").replace('.','').replace(',','.')
                            except IndexError:
                                continue
                            try:
                                debt_EBITDA_2y = debt_EBITDA_values[2].get_attribute("textContent").replace('.','').replace(',','.')
                            except IndexError:
                                continue
                            try:
                                debt_EBITDA_3y = debt_EBITDA_values[3].get_attribute("textContent").replace('.','').replace(',','.')
                            except IndexError:
                                continue
                            '''try:
                                debt_EBITDA_4y = debt_EBITDA_values[4].get_attribute("textContent").replace('.','').replace(',','.')
                            except IndexError:
                                continue
                            try:
                                debt_EBITDA_5y = debt_EBITDA_values[5].get_attribute("textContent").replace('.','').replace(',','.')
                            except IndexError:
                                continue'''
                            print("debt EBITDA history: "  + debt_EBITDA_1y + ' ' + debt_EBITDA_2y + ' ' + debt_EBITDA_3y + ' ' + debt_EBITDA_4y + ' ' + debt_EBITDA_5y)
                        elif "CAGR LUCROS" in indicator.get_attribute("textContent"):
                            cagr_values = item.find_elements(By.CLASS_NAME, "value")
                            try:
                                cagr_1y = cagr_values[1].get_attribute("textContent").replace('.','').replace(',','.').replace('%','')     
                            except IndexError:
                                continue
                            try:
                                cagr_2y = cagr_values[2].get_attribute("textContent").replace('.','').replace(',','.').replace('%','')           
                            except IndexError:
                                continue
                            try:
                                cagr_3y = cagr_values[3].get_attribute("textContent").replace('.','').replace(',','.').replace('%','')           
                            except IndexError:
                                continue
                            '''try:
                                cagr_4y = cagr_values[4].get_attribute("textContent").replace('.','').replace(',','.').replace('%','')           
                            except IndexError:
                                continue
                            try:
                                cagr_5y = cagr_values[5].get_attribute("textContent").replace('.','').replace(',','.').replace('%','')           
                            except IndexError:
                                continue'''
                            print("CAGR history: "  + cagr_1y + ' ' + cagr_2y + ' ' + cagr_3y + ' ' + cagr_4y + ' ' + cagr_5y)
                except TimeoutException:
                    print("at least one element not found by the driver")
                
                
                #find indicators
                fundamentalist_indicators = driver.find_element(By.ID, "table-indicators")
                fundamentalist_indicators_cells = fundamentalist_indicators.find_elements(By.CLASS_NAME, "cell")
                for item in fundamentalist_indicators_cells:
                    cell_fields = item.find_elements(By.XPATH, "./*")
                    if cell_fields[0].get_attribute("textContent") == "DÍVIDA LÍQUIDA / EBITDA ":
                        debt_EBITDA = cell_fields[1].find_element(By.XPATH, "./*").get_attribute("textContent").replace('.', '').replace(',', '.').replace('\t','').replace(' ', '').replace('%','').replace('\n','')
                        print("divida liquida/EBITDA: ",end='')
                        print(debt_EBITDA)
                    elif cell_fields[0].get_attribute("textContent") == "PAYOUT ":
                        payout = cell_fields[1].find_element(By.XPATH, "./*").get_attribute("textContent").replace('.', '').replace(',', '.').replace('\t','').replace(' ', '').replace('%','').replace('\n','')
                        print("Payout: ",end='')
                        print(payout)
                    elif cell_fields[0].get_attribute("textContent") == "ROE ":
                        roe = cell_fields[1].find_element(By.XPATH, "./*").get_attribute("textContent").replace('.', '').replace(',', '.').replace('\t','').replace(' ', '').replace('%','').replace('\n','')
                        print("ROE: ",end='')
                        print(roe)
                    elif cell_fields[0].get_attribute("textContent") == "ROIC ":
                        roic = cell_fields[1].find_element(By.XPATH, "./*").get_attribute("textContent").replace('.', '').replace(',', '.').replace('\t','').replace(' ', '').replace('%','').replace('\n','')
                        print("ROIC : ",end='')
                        print(roic)
                    elif cell_fields[0].get_attribute("textContent") == "P/L ":
                        pl = cell_fields[1].find_element(By.XPATH, "./*").get_attribute("textContent").replace('.', '').replace(',', '.').replace('\t','').replace(' ', '').replace('%','').replace('\n','')
                        print("PL : ",end='')
                        print(pl)
                    elif cell_fields[0].get_attribute("textContent") == "EV/EBIT ":
                        ev_ebit = cell_fields[1].find_element(By.XPATH, "./*").get_attribute("textContent").replace('.', '').replace(',', '.').replace('\t','').replace(' ', '').replace('%','').replace('\n','')
                        print("EV/EBIT: ",end='')
                        print(ev_ebit)
                    elif cell_fields[0].get_attribute("textContent") == "CAGR LUCROS 5 ANOS ":
                        cagr = cell_fields[1].find_element(By.XPATH, "./*").get_attribute("textContent").replace('.', '').replace(',', '.').replace('\t','').replace(' ', '').replace('%','').replace('\n','')
                        print("CAGR profits 5 years: ",end='')
                        print(cagr)
                    elif cell_fields[0].get_attribute("textContent") == "P/VP ":
                        pvp = cell_fields[1].find_element(By.XPATH, "./*").get_attribute("textContent").replace('.', '').replace(',', '.').replace('\t','').replace(' ', '').replace('%','').replace('\n','')
                        print("P/VP: ",end='')
                        print(pvp)
                    elif "DIVIDEND YIELD" in cell_fields[0].get_attribute("textContent"):
                        dy = cell_fields[1].find_element(By.XPATH, "./*").get_attribute("textContent").replace('.', '').replace(',', '.').replace('\t','').replace(' ', '').replace('%','').replace('\n','')
                        print("DY: ",end='')
                        print(dy)
                    elif cell_fields[0].get_attribute("textContent") == "LPA ":
                        lpa = cell_fields[1].find_element(By.XPATH, "./*").get_attribute("textContent").replace('.', '').replace(',', '.').replace('\t','').replace(' ', '').replace('%','').replace('\n','')
                        print("LPA: ",end='')
                        print(lpa)
                    elif cell_fields[0].get_attribute("textContent") == "VPA ":
                        vpa = cell_fields[1].find_element(By.XPATH, "./*").get_attribute("textContent").replace('.', '').replace(',', '.').replace('\t','').replace(' ', '').replace('%','').replace('\n','')
                        print("VPA: ",end='')
                        print(vpa)


                row_to_write = {"company": stock["name"], 
                                "current_price": current_price,
                                "liquidity": liquidity, 
                                "ev": ev,
                                "sector": sector,
                                "segment": segment,
                                "profit_last_year": profit_last_year, 
                                "profit_2y": profit_2y, 
                                "profit_3y": profit_3y,
                                "profit_4y": profit_4y,
                                "profit_5y": profit_5y,
                                "ebit": ebit,
                                "payout (%)": payout,
                                "divida_EBITDA": debt_EBITDA,
                                "divida_EBITDA_1y": debt_EBITDA_1y,
                                "divida_EBITDA_2y": debt_EBITDA_2y,
                                "divida_EBITDA_3y": debt_EBITDA_3y,
                                "divida_EBITDA_4y": debt_EBITDA_4y,
                                "divida_EBITDA_5y": debt_EBITDA_5y,
                                "roe (%)": roe,
                                "roe_1y (%)": roe_1y,
                                "roe_2y (%)": roe_2y,
                                "roe_3y (%)": roe_3y,
                                "roe_4y (%)": roe_4y,
                                "roe_5y (%)": roe_5y,
                                "roic (%)": roic, 
                                "vpa": vpa,
                                "lpa": lpa,
                                "pl": pl, 
                                "pl_1y": pl_1y,
                                "pl_2y": pl_2y,
                                "pl_3y": pl_3y,
                                "pl_4y": pl_4y,
                                "pl_5y": pl_5y,
                                "ev_ebit": ev_ebit, 
                                "cagr (%)": cagr,
                                "cagr_1y (%)": cagr_1y,
                                "cagr_2y (%)": cagr_2y,
                                "cagr_3y (%)": cagr_3y,
                                "cagr_4y (%)": cagr_4y,
                                "cagr_5y (%)": cagr_5y,
                                "pvp": pvp,
                                "pvp_1y": pvp_1y,
                                "pvp_2y": pvp_2y,
                                "pvp_3y": pvp_3y,
                                "pvp_4y": pvp_4y,
                                "pvp_5y": pvp_5y,
                                "dy (%)": dy
                                }
                writer.writerow(row_to_write)
                print("row to write: ")
                print (row_to_write)
            else:
                print("year of beginning is too recent")
                print(year_beginning)
                print(stock["name"])
                print(stock["URL"])
                continue

print()
print("end")

driver.quit()
