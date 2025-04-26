import csv

NO_DATA = -999999

def rank_stocks(max_score, stock_list, stocks_scores, key):
    score = max_score
    for item in stock_list:
        if item[key] != NO_DATA:
            #print (item['company'], end=' ')
           # print(item[key], end=' ')             
            for company in stocks_scores:
                if company['name'] == item['company']:
                    company['score'] += score
                    score -= 1
                    #print(company['score'])
        #elif item[key] == NO_DATA:
        #    print()

#creates new list and sorts it using the key column
def sort_by(stock_list, key):
    current_stocks_sorted = sorted(stock_list, key=lambda row: float(row[key]))
    return current_stocks_sorted

def analyze_set(current_stocks, current_segment):
    print(current_segment)

    max_score = len(current_stocks)
    stocks_scores = []
    for stock in current_stocks:
        stocks_scores.append(
            {
                "name": stock['company'],
                "score": 0
            }
        )
    
    #replace empty cells with NO_DATA
    for stock in current_stocks:
        for key, value in stock.items():
            if value == "-":
                #print("aaaaaaaaaaaaaaa")
                stock[key] = NO_DATA

    #print('pl: ')
    current_stocks_sorted = sort_by(current_stocks, 'pl')
    rank_stocks(max_score, current_stocks_sorted, stocks_scores, 'pl')

    #print('pvp: ')
    current_stocks_sorted = sort_by(current_stocks, 'pvp')
    rank_stocks(max_score, current_stocks_sorted, stocks_scores, 'pvp')

    #print('roe: ')
    current_stocks_sorted = sort_by(current_stocks, 'roe')
    current_stocks_sorted.reverse()
    rank_stocks(max_score, current_stocks_sorted, stocks_scores, 'roe')

    #print('divida EBITDA: ')
    current_stocks_sorted = sort_by(current_stocks, 'divida_EBITDA')
    rank_stocks(max_score, current_stocks_sorted, stocks_scores, 'divida_EBITDA')


    #print('cagr: ')
    current_stocks_sorted = sort_by(current_stocks, 'cagr')
    current_stocks_sorted.reverse()
    rank_stocks(max_score, current_stocks_sorted, stocks_scores, 'cagr')

    stocks_scores_sorted = sorted(stocks_scores, key=lambda row: float(row['score']))
    stocks_scores_sorted.reverse()
    print('final score: ')
    for stock in stocks_scores_sorted:
        print(stock['name'], end=' ')
        print(stock['score'])

    print()

sorted_rows = []
reader = []

#read data from output file and sort by sector and segment
with open("stocks_data.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)
    sorted_rows = sorted(rows, key=lambda row: (row['sector'], row['segment']))
    rows_to_remove = []
    for row in sorted_rows:
        #print(row['company'] + ' ' + row['liquidity'])
        liq = row['liquidity'].replace('.', '')
        if liq != "-":
           if float(liq) < 3000000:
                rows_to_remove.append(row)
                #print("weima")
                #print(row['company'] + ' ' + row['liquidity'])
    for row in rows_to_remove:
        sorted_rows.remove(row)

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
    #print(current_segment)
    for row in rows:
        try:
            #filter out liquidity < 3M, 
            if row['segment'] == current_segment:
                current_stocks.append(row)
            else: 
                analyze_set(current_stocks, current_segment)
                current_segment = row['segment']

                

                current_stocks.clear()
                current_stocks.append(row)
            
        except ValueError:
            # Skip rows with invalid numbers
            print('VALUE ERROR')
            continue
    analyze_set(current_stocks, current_segment)
