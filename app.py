from tabulate import tabulate
from datetime import date

import yfinance as yf
import json

today = date.today()

stocksTracking = ["USO", "IXC", "UCO", "WTI", "AAL", "NCLH", "SAVE", "DIS", "APA"]
stocksOwned = [322, 66, 124, 455, 12, 168, 70, 22, 31]

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
    "52weekChange": abs(cYrPrice),
    "sharesOwned": stocksOwned[cnt],
    "sharesOwnedVal": stocksOwned[cnt] * cPrice,
    "sharesOwnedPredicted": stocksOwned[cnt] * oneYear,
  }
  sData[s]["tabulateData"] = [s, sData[s]["close"], sData[s]["52weekPrice"], sData[s]["52weekChange"], sData[s]["sharesOwned"], sData[s]["sharesOwnedVal"], sData[s]["sharesOwnedPredicted"]]

  print(f"sData[s]['52weekChange'] = {sData[s]['52weekChange']}")
  cnt += 1

# tabulate
table = []
table.append(["ticker", "close", "52weekPrice", "52weekChange", "sharesOwned", "sharesOwnedVal", "sharesOwnedPredicted"])
for k, v in sData.items():
  table.append(v["tabulateData"])

print(tabulate(table, headers="firstrow"))

# find totals
sovSum = 0.0
for k, v in sData.items():
  sovSum += v["sharesOwnedVal"]

print(f"total value of shares owned: {sovSum}")