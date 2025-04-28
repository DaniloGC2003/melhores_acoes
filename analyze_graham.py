import csv
import math

NO_DATA = -999999

sorted_rows = []
good_stocks = []
reader = []

#read data from output file and sort by sector and segment
with open("stocks_data.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)
    sorted_rows = sorted(rows, key=lambda row: (row['sector'], row['segment']))
    #replace empty cells with NO_DATA
    for stock in sorted_rows:
        for key, value in stock.items():
            if value == "-":
                stock[key] = NO_DATA
    print('rows to remove: ')
    for row in sorted_rows:
        #print(row['company'] + ' ' + row['liquidity'])
        liq = row['liquidity']
        profit_last_year = row['profit_last_year']
        profit_2y = row['profit_2y']
        profit_3y = row['profit_3y']
        profit_4y = row['profit_4y']
        profit_5y = row['profit_5y']
        current_price = row['current_price']
        current_pl = row['pl']
        current_pvp = row['pvp']
        graham = 0
        if float(row['lpa']) > 0 and float(row['vpa']) > 0:
            graham = math.sqrt(float(row['lpa']) * float(row['vpa']) * 22.5)
        else:
            graham = NO_DATA

        if float(liq) > 3000000:
            if float(profit_last_year) > 0 and float(profit_2y) > 0 and float(profit_3y) > 0 and float(profit_4y) > 0 and float(profit_5y) > 0:
                if float(current_price) < float(graham):
                    good_stocks.append(row)
                else:
                    print(row['company'])
        
    print()


#store sorted and filtered data
with open("stocks_data_graham.csv", 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=reader.fieldnames)
    writer.writeheader()
    writer.writerows(good_stocks)

with open("stocks_data_graham.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)
    for row in rows:
        print(row['company'])


