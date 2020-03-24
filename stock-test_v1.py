from yahoo_fin import stock_info as si
import pandas as pd
import json
import csv
import functools
from prettytable import PrettyTable

tickers = []
valor = []
quantidade = []
gainloss = 0

with open('position.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))

for line in data:
    linha = (line[0].split(";"))
    tickers.append(linha[0])
    quantidade.append(linha[1])
    valor.append(linha[2])
#print(tickers)
#print(quantidade)
#print(valor)
while 1:
    t = PrettyTable()
    t.field_names = ["Ticker", "qtd", "pago", "atual"]
    for x in range(len(tickers)):
        valoratual = si.get_live_price(tickers[x])
        lucrototal = int(quantidade[x]) * (valoratual - float(valor[x]))
        t.add_row([tickers[x], quantidade[x],round(int(quantidade[x])*float(valor[x]),2), round(int(quantidade[x])*float(valoratual),2)])
        #print(tickers[x])
        gainloss+= float(lucrototal)
    print(t)
    print(gainloss)
    gainloss = 0
    print("\n")


"""
data = pd.read_csv("position.csv")
jason = data.to_json(orient='records', lines=True)
print(jason)
y = json.loads(jason)
print(y)
"""





