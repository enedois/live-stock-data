from yahoo_fin import stock_info as si
import pandas as pd
import csv
from prettytable import PrettyTable
import threading
from playsound import playsound

tickers = []
valor = []
quantidade = []
gainloss = 0
maiorgain = -99999999999999

def sound():
    for x in range(1):
        playsound('alert.wav')
        

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
    t.field_names = ["Ticker", "qtd", "pago", "atual","%"]
    for x in range(len(tickers)):
        valoratual = si.get_live_price(tickers[x])
        lucrototal = int(quantidade[x]) * (valoratual - float(valor[x]))
        lucroinicial = round(int(quantidade[x])*float(valor[x]),2)
        lucroatual = round(int(quantidade[x])*float(valoratual),2)
        t.add_row([tickers[x], quantidade[x], lucroinicial, lucroatual,'{:.1%}'.format((lucroatual/lucroinicial)-1)])
        #print(tickers[x])
        gainloss+= float(lucrototal)
    if(gainloss>maiorgain):
        maiorgain=gainloss
    print(t)
    print("Saldo: "+str(gainloss))
    print("Maior Gain: "+str(maiorgain))
    print("Diff: "+str(maiorgain-gainloss))
    if((maiorgain-gainloss)==0):
        threading.Thread(target=sound, args=()).start()
    gainloss = 0
    print("\n")





