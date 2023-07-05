def round_price(price):
  if price >= 1:
    return round(price, 2)
  elif price >= 0.0001:
    return round(price, 6)
  elif price >= 0.000001:
    return round(price, 8)
  elif price >= 0.00000001:
    return round(price, 10)
  else:
    return round(price, 12)


def format_coin_data(coin_data):
  try:
    symbol = coin_data['symbol']
    name = coin_data['name']
    price = round_price(coin_data['quote']['USD']['price'])
    volume_24h = coin_data['quote']['USD']['volume_24h']
    percent_change_1h = coin_data['quote']['USD']['percent_change_1h']
    percent_change_24h = coin_data['quote']['USD']['percent_change_24h']
    percent_change_7d = coin_data['quote']['USD']['percent_change_7d']
    market_cap = coin_data['quote']['USD']['market_cap']

    formatted_data = f"Symbol: {symbol}\nName: {name}\nPrice: {price} USD\nVolume (24h): {volume_24h}\n" \
                     f"Percent Change (1h): {percent_change_1h}\nPercent Change (24h): {percent_change_24h}\n" \
                     f"Percent Change (7d): {percent_change_7d}\nMarket Cap: {market_cap} USD"

    return formatted_data
  except KeyError:
    return "Failed to fetch coin data."


def format_favorite_coins(coins):
  formatted_coins = []

  for index, coin in enumerate(coins, start=1):
    try:
      name = coin['name']
      symbol = coin['symbol']
      price = round_price(coin['quote']['USD']['price'])
      formatted_coin = f'{index}. {name} ({symbol}) : {price} USD'
      formatted_coins.append(formatted_coin)
    except KeyError:
      formatted_coins.append(f'{index}. Failed to fetch coin data.')

  return '\n'.join(formatted_coins)
