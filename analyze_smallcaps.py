import csv
import math

smll_tickers = [
    "RRRP3", "TTEN3", "ABCB4", "AESB3", "AALR3", "ALOS3", "ALPA4", "ALUP11",
    "AMBP3", "ANIM3", "ARZZ3", "ARML3", "AZUL4", "BPAN4", "BRSR6", "BMOB3",
    "BLAU3", "BRAP4", "AGRO3", "CAML3", "CASH3", "CBAV3", "CEAB3", "CIEL3",
    "CLSA3", "COGN3", "CSMG3", "CURY3", "CVCB3", "CYRE3", "DASA3", "DIRR3",
    "DXCO3", "ECOR3", "ENAT3", "EVEN3", "EZTC3", "FESA4", "FLRY3", "FRAS3",
    "GFSA3", "GGPS3", "GOAU4", "GRND3", "GUAR3", "HBSA3", "IFCM3", "IGTI11",
    "INTB3", "IRBR3", "JALL3", "JHSF3", "KEPL3", "LAVV3", "LEVE3", "LJQQ3",
    "LOGG3", "LWSA3", "MATD3", "MBLY3", "MDIA3", "MILS3", "MLAS3", "MOVI3",
    "MRFG3", "MRVE3", "MTRE3", "MYPK3", "ODPV3", "ONCO3", "ORVR3", "PCAR3",
    "PETZ3", "PGMN3", "PNVL3", "POMO4", "PTBL3", "POSI3", "QUAL3", "RANI3",
    "RAPT4", "RCSL3", "RECV3", "ROMI3", "SAPR11", "SBFG3", "SEER3", "SIMH3",
    "SLCE3", "SMFT3", "SMTO3", "SOMA3", "TAEE11", "TASA4", "TGMA3", "TEND3",
    "TRAD3", "TRIS3", "TUPY3", "UNIP6", "USIM3", "USIM5", "VIVA3", "VLID3",
    "VULC3", "WIZC3", "YDUQ3", "ZAMP3"
]

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
        pass
        #print(row['company'], end=' ')
        #print(row['cagr (%)'])

    

    #sorted_rows.reverse()
    '''for row in sorted_rows:
        if float(row['liquidity']) > 3000000:
            if row['sector'] != 'Financeiro':
                if float(row['ebit']) > 0:
                    if float(row['profit_last_year']) > 0 and float(row['profit_2y']) > 0 and float(row['profit_3y']) > 0 and float(row['profit_4y']) > 0 and float(row['profit_5y']) > 0: 
                        good_stocks.append(row)'''
    
    for row in sorted_rows:
        if row['company'].split()[-1] in smll_tickers:
            if row['sector'] != 'Financeiro':
                if float(row['profit_last_year']) > 0 and float(row['profit_2y']) > 0 and float(row['profit_3y']) > 0: 
                    if float(row['ebit']) > 0 and float(row['roe (%)']) > 10 and float(row['cagr (%)']) > 10:
                        print(row['company'])
                        good_stocks.append(row)

    print()


#store sorted and filtered data
with open("stocks_data_smallcaps.csv", 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=reader.fieldnames)
    writer.writeheader()
    writer.writerows(good_stocks)

with open("stocks_data_smallcaps.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)
    for row in rows:
        print(row['company'])