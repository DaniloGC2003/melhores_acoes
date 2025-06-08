import csv
import math

NO_DATA = -999999

sorted_rows = []
good_stocks = []
reader = []
#read data from output file and sort by cagr
with open("stocks_data.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)
    #replace empty cells with NO_DATA
    for stock in rows:
        for key, value in stock.items():
            if value == "-":
                stock[key] = NO_DATA
    sorted_rows = sorted(rows, key=lambda row: float(row['cagr (%)']))
    for row in sorted_rows:
        print(row['company'], end=' ')
        print(row['cagr (%)'])

    

    #sorted_rows.reverse()
    '''for row in sorted_rows:
        if float(row['liquidity']) > 3000000:
            if row['sector'] != 'Financeiro':
                if float(row['ebit']) > 0:
                    if float(row['profit_last_year']) > 0 and float(row['profit_2y']) > 0 and float(row['profit_3y']) > 0 and float(row['profit_4y']) > 0 and float(row['profit_5y']) > 0: 
                        good_stocks.append(row)'''
    for row in sorted_rows:
        if float(row['liquidity']) > 3000000:
            if row['sector'] != 'Financeiro':
                if float(row['profit_last_year']) > 0 and float(row['profit_2y']) > 0 and float(row['profit_3y']) > 0: 
                    if float(row['ebit']) > 0:
                        if float(row['divida_EBITDA']) < 3:
                            good_stocks.append(row)

    print()


#store sorted and filtered data
with open("stocks_data_cheapest.csv", 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=reader.fieldnames)
    writer.writeheader()
    writer.writerows(good_stocks)

with open("stocks_data_cheapest.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)
    for row in rows:
        print(row['company'])