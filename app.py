from tabulate import tabulate
from datetime import date

import yfinance as yf
import json

today = date.today()

stocksTracking = ["USO", "IXC", "UCO", "WTI", "AAL", "NCLH", "SAVE", "DIS", "APA"]
stocksOwned = [312, 166, 66, 4, 0, 0, 0, 0, 0]

sData = {}
cnt = 0
for s in stocksTracking:
  temp = yf.Ticker(s)
  cPrice = temp.info["regularMarketPreviousClose"]
  cYrPrice = temp.info["52WeekChange"]
  if cYrPrice is None:
    cYrPrice = 1
  if cPrice is None:
    cPrice = 1
  oneYear = cPrice - (cPrice * cYrPrice)
  print(s)
  print(cPrice)
  print(cYrPrice)
  sData[s] = {
    "close": cPrice,
    "52weekPrice": oneYear,
    "52weekChange": cYrPrice,
    "sharesOwned": stocksOwned[cnt],
    "sharesOwnedVal": stocksOwned[cnt] * cPrice,
    "sharesOwnedPredicted": stocksOwned[cnt] * cYrPrice,
    "tabulateData": [s, cPrice, oneYear, cYrPrice, stocksOwned[cnt], stocksOwned[cnt] * cPrice, stocksOwned[cnt] * cYrPrice]
  }
  cnt += 1

# tabulate
table = []
table.append(["ticker", "close", "52weekPrice", "52weekChange", "sharesOwned", "sharesOwnedVal", "sharesOwnedPredicted"])
for k, v in sData.items():
  table.append(v["tabulateData"])

print(tabulate(table, headers="firstrow"))