import csv

with open("stocks_data.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        try:
            liquidity = float(row["liquidity"].replace('.', ''))
            profit_last_year = float(row["profit_last_year"].replace('.', ''))
            profit_2y = float(row["profit_2y"].replace('.', ''))
            profit_3y = float(row["profit_3y"].replace('.', ''))
            payout = 0
            payout_str = row["payout"]
            #print(payout_str)
            if payout_str != '-':
                payout = float(row["payout"].replace(',','.')[:-1])
                #print(payout)
            else:
                payout = "no payout"
            
            if liquidity > 3_000_000:
                if profit_last_year > profit_2y and profit_2y > profit_3y:
                    if payout != "no payout":
                        if payout >= 30.00 and payout <= 500:
                            print(row)

        except ValueError:
            # Skip rows with invalid numbers
            continue