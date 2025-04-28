import csv
import math

NO_DATA = -999999

def find_avg_cagr(stock):
    #print(stock['company'])
    cagr_sum = 0
    cagr_terms = 0
    if stock['cagr (%)'] != NO_DATA:
        cagr_sum += float(stock['cagr (%)'])
        cagr_terms += 1
    if stock['cagr_1y (%)'] != NO_DATA:
        cagr_sum += float(stock['cagr_1y (%)'])
        cagr_terms += 1
    if stock['cagr_2y (%)'] != NO_DATA:
        cagr_sum += float(stock['cagr_2y (%)'])
        cagr_terms += 1
    if stock['cagr_3y (%)'] != NO_DATA:
        cagr_sum += float(stock['cagr_3y (%)'])
        cagr_terms += 1
    if stock['cagr_4y (%)'] != NO_DATA:
        cagr_sum += float(stock['cagr_4y (%)'])
        cagr_terms += 1
    if stock['cagr_5y (%)'] != NO_DATA:
        cagr_sum += float(stock['cagr_5y (%)'])
        cagr_terms += 1
    
    if cagr_terms != 0:
        return cagr_sum / cagr_terms
    else:
        return NO_DATA

def find_avg_debt_EBITDA(stock):
    #print(stock['company'])
    divida_EBITDA_sum = 0
    divida_EBITDA_terms = 0
    if stock['divida_EBITDA'] != NO_DATA:
        divida_EBITDA_sum += float(stock['divida_EBITDA'])
        divida_EBITDA_terms += 1
    if stock['divida_EBITDA_1y'] != NO_DATA:
        divida_EBITDA_sum += float(stock['divida_EBITDA_1y'])
        divida_EBITDA_terms += 1
    if stock['divida_EBITDA_2y'] != NO_DATA:
        divida_EBITDA_sum += float(stock['divida_EBITDA_2y'])
        divida_EBITDA_terms += 1
    if stock['divida_EBITDA_3y'] != NO_DATA:
        divida_EBITDA_sum += float(stock['divida_EBITDA_3y'])
        divida_EBITDA_terms += 1
    if stock['divida_EBITDA_4y'] != NO_DATA:
        divida_EBITDA_sum += float(stock['divida_EBITDA_4y'])
        divida_EBITDA_terms += 1
    if stock['divida_EBITDA_5y'] != NO_DATA:
        divida_EBITDA_sum += float(stock['divida_EBITDA_5y'])
        divida_EBITDA_terms += 1
    
    if divida_EBITDA_terms != 0:
        return divida_EBITDA_sum / divida_EBITDA_terms
    else:
        return NO_DATA

def find_avg_roe(stock):
    #print(stock['company'])
    roe_sum = 0
    roe_terms = 0
    if stock['roe (%)'] != NO_DATA:
        roe_sum += float(stock['roe (%)'])
        roe_terms += 1
    if stock['roe_1y (%)'] != NO_DATA:
        roe_sum += float(stock['roe_1y (%)'])
        roe_terms += 1
    if stock['roe_2y (%)'] != NO_DATA:
        roe_sum += float(stock['roe_2y (%)'])
        roe_terms += 1
    if stock['roe_3y (%)'] != NO_DATA:
        roe_sum += float(stock['roe_3y (%)'])
        roe_terms += 1
    if stock['roe_4y (%)'] != NO_DATA:
        roe_sum += float(stock['roe_4y (%)'])
        roe_terms += 1
    if stock['roe_5y (%)'] != NO_DATA:
        roe_sum += float(stock['roe_5y (%)'])
        roe_terms += 1
    
    if roe_terms != 0:
        return roe_sum / roe_terms
    else:
        return NO_DATA

def find_avg_pvp(stock):
    #print(stock['company'])
    pvp_sum = 0
    pvp_terms = 0
    if stock['pvp'] != NO_DATA:
        pvp_sum += float(stock['pvp'])
        pvp_terms += 1
    if stock['pvp_1y'] != NO_DATA:
        pvp_sum += float(stock['pvp_1y'])
        pvp_terms += 1
    if stock['pvp_2y'] != NO_DATA:
        pvp_sum += float(stock['pvp_2y'])
        pvp_terms += 1
    if stock['pvp_3y'] != NO_DATA:
        pvp_sum += float(stock['pvp_3y'])
        pvp_terms += 1
    if stock['pvp_4y'] != NO_DATA:
        pvp_sum += float(stock['pvp_4y'])
        pvp_terms += 1
    if stock['pvp_5y'] != NO_DATA:
        pvp_sum += float(stock['pvp_5y'])
        pvp_terms += 1
    
    if pvp_terms != 0:
        return pvp_sum / pvp_terms
    else:
        return NO_DATA
    
def find_avg_pl(stock):
    #print(stock['company'])
    pl_sum = 0
    pl_terms = 0
    if stock['pl'] != NO_DATA:
        pl_sum += float(stock['pl'])
        pl_terms += 1
    if stock['pl_1y'] != NO_DATA:
        pl_sum += float(stock['pl_1y'])
        pl_terms += 1
    if stock['pl_2y'] != NO_DATA:
        pl_sum += float(stock['pl_2y'])
        pl_terms += 1
    if stock['pl_3y'] != NO_DATA:
        pl_sum += float(stock['pl_3y'])
        pl_terms += 1
    if stock['pl_4y'] != NO_DATA:
        pl_sum += float(stock['pl_4y'])
        pl_terms += 1
    if stock['pl_5y'] != NO_DATA:
        pl_sum += float(stock['pl_5y'])
        pl_terms += 1
    
    if pl_terms != 0:
        return pl_sum / pl_terms
    else:
        return NO_DATA

#rank stocks by the key column
#the first stock in the list gets the highest score, the last one the lowest
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
    segment_avg_pl = 0
    count_pl = 0
    segment_avg_pvp = 0
    count_pvp = 0
    segment_avg_roe = 0
    count_roe = 0
    segment_avg_debt_EBITDA = 0
    count_debt_EBITDA = 0
    segment_avg_cagr = 0
    count_cagr = 0

    max_score = len(current_stocks)
    stocks_scores = []
    for stock in current_stocks:
        #create a list of stocks with their scores
        stocks_scores.append(
            {
                "name": stock['company'],
                "score": 0,
                "segment": stock['segment'],
            }
        )
        #replace empty cells with NO_DATA
        for key, value in stock.items():
            if value == "-":
                stock[key] = NO_DATA

        #find average values for each indicator
        avg_pl = find_avg_pl(stock)
        #print('avg_pl: ', end='')
        #print(avg_pl)
        if avg_pl != NO_DATA:
            segment_avg_pl += avg_pl
            count_pl += 1
        avg_pvp = find_avg_pvp(stock)
        #print('avg_pvp: ', end='')
        #print(avg_pvp)
        if avg_pvp != NO_DATA:
            segment_avg_pvp += avg_pvp
            count_pvp += 1
        avg_roe = find_avg_roe(stock)
        #print('avg_roe: ', end='')
        #print(avg_roe)
        if avg_roe != NO_DATA:
            segment_avg_roe += avg_roe
            count_roe += 1
        avg_debt_EBITDA = find_avg_debt_EBITDA(stock)
        #print('avg_debt_EBITDA: ', end='')
        #print(avg_debt_EBITDA)
        if avg_debt_EBITDA != NO_DATA:
            segment_avg_debt_EBITDA += avg_debt_EBITDA
            count_debt_EBITDA += 1
        avg_cagr = find_avg_cagr(stock)
        #print('avg_cagr: ', end='')
        #print(avg_cagr)
        if avg_cagr != NO_DATA:
            segment_avg_cagr += avg_cagr
            count_cagr += 1
    if count_pl != 0:
        segment_avg_pl /= count_pl
    if count_pvp != 0:
        segment_avg_pvp /= count_pvp
    if count_roe != 0:
        segment_avg_roe /= count_roe
    if count_debt_EBITDA != 0:
        segment_avg_debt_EBITDA /= count_debt_EBITDA
    if count_cagr != 0:
        segment_avg_cagr /= count_cagr


    '''print('average pl: ', end='')
    print(segment_avg_pl)
    print('average pvp: ', end='')
    print(segment_avg_pvp)
    print('average roe: ', end='')
    print(segment_avg_roe)
    print('average debt_EBITDA: ', end='')
    print(segment_avg_debt_EBITDA)
    print('average cagr: ', end='')
    print(segment_avg_cagr)'''


    
    #print('pl: ')
    current_stocks_sorted = sort_by(current_stocks, 'pl')
    rank_stocks(max_score, current_stocks_sorted, stocks_scores, 'pl')

    #print('pvp: ')
    current_stocks_sorted = sort_by(current_stocks, 'pvp')
    rank_stocks(max_score, current_stocks_sorted, stocks_scores, 'pvp')

    #print('roe: ')
    current_stocks_sorted = sort_by(current_stocks, 'roe (%)')
    current_stocks_sorted.reverse()
    rank_stocks(max_score, current_stocks_sorted, stocks_scores, 'roe (%)')

    #print('divida EBITDA: ')
    current_stocks_sorted = sort_by(current_stocks, 'divida_EBITDA')
    rank_stocks(max_score, current_stocks_sorted, stocks_scores, 'divida_EBITDA')

    #print('cagr: ')
    current_stocks_sorted = sort_by(current_stocks, 'cagr (%)')
    current_stocks_sorted.reverse()
    rank_stocks(max_score, current_stocks_sorted, stocks_scores, 'cagr (%)')

    stocks_scores_sorted = sorted(stocks_scores, key=lambda row: float(row['score']))
    stocks_scores_sorted.reverse()

    stocks_first_in_segment.append(stocks_scores_sorted[0])
    print('final score: ')
    for stock in stocks_scores_sorted:
        print(stock['name'], end=' ')
        print(stock['score'])
    #print('best stocks: ')
    #see how many indicators are above average for each stock
    for stock in current_stocks_sorted:
        above_average_indicators = 0
        if (float(stock['pl']) < segment_avg_pl):
            above_average_indicators += 1
        if (float(stock['pvp']) < segment_avg_pvp):
            above_average_indicators += 1
        if (float(stock['roe (%)']) > segment_avg_roe):
            above_average_indicators += 1
        if (float(stock['divida_EBITDA']) < segment_avg_debt_EBITDA):   
            above_average_indicators += 1
        if (float(stock['cagr (%)']) > segment_avg_cagr):
            above_average_indicators += 1
        if (above_average_indicators >= 5):
            #print(stock['company'])
            stocks_above_avg_indicators.append(stock)

    print()

sorted_rows = []
reader = []

stocks_above_avg_indicators = []
stocks_first_in_segment = []


#read data from output file and sort by sector and segment
with open("stocks_data.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)
    sorted_rows = sorted(rows, key=lambda row: (row['sector'], row['segment']))
    rows_to_remove = []
    for row in sorted_rows:
        #print(row['company'] + ' ' + row['liquidity'])
        liq = row['liquidity'].replace('.', '')
        profit_last_year = row['profit_last_year']
        profit_2y = row['profit_2y']
        profit_3y = row['profit_3y']
        profit_4y = row['profit_4y']
        profit_5y = row['profit_5y']
        current_price = row['current_price']
        #graham = math.sqrt(float(row['lpa']) * float(row['vpa']) * 22.5)
        if liq != "-":
           if float(liq) < 3000000 or float(profit_last_year) < 0 or float(profit_2y) < 0 or float(profit_3y) < 0 or float(profit_4y) < 0 or float(profit_5y) < 0 or float(graham) < float(current_price):
                rows_to_remove.append(row)
                #print("weima")
                #print(row['company'] + ' ' + row['liquidity'])
    print('rows to remove: ')
    for row in rows_to_remove:
        print(row['company'])
        sorted_rows.remove(row)

#store sorted and filtered data
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

print('above average indicators: ')
for stock in stocks_above_avg_indicators:
    print(stock['company'])
print()
print('first in segment: ')
for stock in stocks_first_in_segment:
    print(stock['name'], end='\t\t\t\t\t')
    print(stock['segment'])
    
