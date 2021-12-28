import requests
import json

# to get crypto price from bianance API
def getPrices(symbol):
  parameters = {
  'symbol':symbol
  }
  URL = 'https://api.binance.com/api/v3/avgPrice'
  r = requests.get(url=URL, params=parameters)
  data = r.json()
  # Fetching Price
  currencyPrice = float(data["price"])
  # Rounding off
  if currencyPrice > 1:
    currencyPrice = round(currencyPrice, 2)
  elif currencyPrice > 0.01:
    currencyPrice = round(currencyPrice, 4)
  elif currencyPrice > 0.0001:
    currencyPrice = round(currencyPrice, 6)
  else:
    pass
  # return price 
  return currencyPrice