import csv

NO_DATA = -999999

sorted_rows = []
reader = []

#read data from output file and sort by sector and segment
with open("stocks_data.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)
    sorted_rows = sorted(rows, key=lambda row: (row['sector'], row['segment']))

#store sorted data
with open("stocks_data_segment.csv", 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=reader.fieldnames)
    writer.writeheader()
    writer.writerows(sorted_rows)

with open("stocks_data_segment.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)
    current_stocks = []
    current_segment = rows[0]['segment']
    for row in rows:
        try:
            #current_segment = row['segment']
            #print(row)
            #while row['segment'] == current_segment:
            if row['segment'] == current_segment:
                current_stocks.append(row)
                #print(row['segment'])
            else:
                print(current_segment)
                #max_score = len(current_stocks)
                pl_arr = []
                pvp_arr = []
                roe_arr = []
                debt_EBITDA_arr = []
                cagr_arr = []
                for item in current_stocks:
                    #print(item['company'])
                    pl_arr.append(item['pl'])
                    pvp_arr.append(item['pvp'])
                    roe_arr.append(item['roe'])
                    debt_EBITDA_arr.append(item['divida_EBITDA'])
                    cagr_arr.append(item['cagr'])

                #replace empty cells with NO_DATA
                for stock in current_stocks:
                    for key, value in stock.items():
                        if value == "-":
                            stock[key] = NO_DATA

                current_stocks_sorted = sorted(current_stocks, key=lambda row: float(row['pl']))
                print()
                for item in current_stocks_sorted:
                    print (item['company'], end=' ')
                    print(item['pl'])


                current_segment = row['segment']

                

                current_stocks.clear()
                current_stocks.append(row)
                print()
        except ValueError:
            # Skip rows with invalid numbers
            print('VALUE ERROR')
            continue