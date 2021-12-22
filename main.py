import os
import discord
from priceFetching import *

# Initiate a discord client
client = discord.Client()

# Bot Name
botName = "Jiya"

# Call to print console messege after successful login
@client.event
async def on_ready():
  print(f"You have successfully logged in as {client}")
# End of bot configuration
  await discord.utils.get(client.get_all_channels(),name='bot').send(f"{botName} is Logged in.")


# Return crypto currency price whenever there in messege
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  # send crypto currency price from coin market cap updates after 60 sec
  if message.content.startswith('p'):
    # try:
    #   # Requested Currency
    #   requestedData = message.content.lower()[1:]
    #   # Fetching Currency Symbol
    #   #currencySymbol = (getCmcQuotesBySymbol(message.content.lower()[1:])["data"][message.content.upper()[1:]]["name"])
    #   # Fetching currency CMC ID
    #   currencyID = str(list((getCmcQuotesBySlug(message.content.lower()[1:])['data']).keys()))[2:-2]
    #   # Fetching Currency Price
    #   currencyPrice =getCmcQuotesBySlug(message.content.lower()[1:])["data"][currencyID]["quote"]["USD"]["price"]
    #   # Sending Message
    #   await message.channel.send(f'The price of  {requestedData} is {currencyPrice}')
    # except KeyError:
    #   await message.channel.send(f'Sorry {requestedData} is not supported.')
    try:
      # Requested Currency
      requestedData = message.content.lower()[2:]
      # Fetching Currency Name
      currencyName = (getCmcQuotesBySymbol(message.content.lower()[2:])["data"][message.content.upper()[2:]]["name"])
      # Fetching Currency Price
      currencyPrice = (getCmcQuotesBySymbol(message.content.upper()[2:])["data"][message.content.upper()[2:]]["quote"]["USD"]["price"])
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
  # send crypto currecny trading average price directly from binance
  elif message.content.startswith('t'):
    try:
      # Requested Currency
      requestedData = (message.content.lower()[2:]).upper()
      # Fetching Price
      currencyPrice = eval(getCryptoPrices(requestedData)["price"])
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
      await message.channel.send(f'{requestedData} is currently trading at {currencyPrice}')
    except KeyError:
      await message.channel.send(f'Sorry {requestedData} trading pair is not supported.')

try:
  # Bot Access Token
  BOT_TOKEN = os.environ["BOT_TOKEN"]
  # Run Bot
  client.run(BOT_TOKEN)
except KeyError:
  print("Discord Creditional are not Satisfied")
