import os
import discord
import binance
import coinMarketCap
from keep_alive import keep_alive


# Initiate a discord client
client = discord.Client()


# Bot Name
botName = "Jiya"


# Call to print console message after successful login
@client.event
async def on_ready():
  print(f"You have successfully logged in as {client}")
  # End of bot configuration
  await discord.utils.get(client.get_all_channels(),name='bot').send(f"{botName} is Logged in.")


# Send crypto currency price in discord
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  # send crypto currency price from coin market cap
  if message.content.startswith('p'):
    try:
      # Requested Currency
      requestedData = message.content.lower()[2:]
      # Fetching Currency Name
      currencyName = (coinMarketCap.getPrice(message.content.lower()[2:])["data"][message.content.upper()[2:]]["name"])
      # Fetching Currency Price
      currencyPrice = (coinMarketCap.getPrice(message.content.upper()[2:])["data"][message.content.upper()[2:]]["quote"]["USD"]["price"])
      # Rounding off
      if currencyPrice > 1:
        currencyPrice = round(currencyPrice, 2)
      elif currencyPrice > 0.01:
        currencyPrice = round(currencyPrice, 4)
      elif currencyPrice > 0.0001:
        currencyPrice = round(currencyPrice, 6)
      else:
        pass    
      # Sending Message
      await message.channel.send(f'The price of  {currencyName} is {currencyPrice}')
    except KeyError:
      await message.channel.send(f'Sorry {requestedData} is not supported.')
  # send crypto currency average price directly from binance
  elif message.content.startswith('t'):
    try:
      # Requested Currency
      requestedData = (message.content.lower()[2:]).upper()
      # Fetching Price
      currencyPrice = binance.getPrice(requestedData)
      # Sending Message
      await message.channel.send(f'{requestedData} is currently trading at {currencyPrice}')
    except KeyError:
      await message.channel.send(f'Sorry {requestedData} trading pair is not supported.')
  # Additional Commands
  elif message.content.startswith('$support'):
    # Sending Message
    await message.channel.send(f'This Bot supports more than 15,000 crypto currencies from coin market cap and all trading pairs from binance exchange.')
  elif message.content.startswith('$commands'):
    # Sending Message
    await message.channel.send(f'To fetch price form CoinMarketCap:\np <coin_symbol>\nTo Fetch price from Binance:\nt <trading_pair>')
  elif message.content.startswith('$authors'):
    # Sending Message
    await message.channel.send(f'FA21-BCS-020  Fasiha Arshad')
    await message.channel.send(f'FA21-BCS-023  Hammad Saeedi')
  

# Keep Active
keep_alive()


# Bot Creditionals
try:
  # Bot Access Token
  BOT_TOKEN = os.environ["BOT_TOKEN"]
  # Run Bot
  client.run(BOT_TOKEN)
except KeyError:
  print("Discord Creditional are not Satisfied")