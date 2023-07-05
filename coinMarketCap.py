import os
import requests
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


# cmc api keyA
try:
  CMC_KEY = os.environ['CMC_KEY']
except KeyError:
  print("CoinMarketCap Creditional are not Satisfied")


# to get crypto price from coin market cap API by using symbol
def getPrice(symbol):
  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
  parameters = {
  'symbol':symbol,
  'convert':'USD'
  }
  headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': CMC_KEY,
  }
  session = Session()
  session.headers.update(headers)
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  
  if 'data' in data:
    return data['data'].get(symbol.upper())
  return None