from replit import db
import coinMarketCap
from format import *

async def send_message(channel, message):
    await channel.send(message)

async def check_valid_coin(symbol):
    payload = coinMarketCap.getPrice(symbol)
    return payload is not None

async def add_favorite(client, message, args):
    coin = args.upper()
    server_id = str(message.guild.id)
    user_id = str(message.author.id)

    if server_id not in db:
        db[server_id] = {}

    if user_id not in db[server_id]:
        db[server_id][user_id] = []

    is_valid = await check_valid_coin(coin)

    if is_valid:
        if coin not in db[server_id][user_id]:
            db[server_id][user_id].append(coin)
            await send_message(message.channel, f'{coin} added to your favorites.')
        else:
            await send_message(message.channel, f'{coin} is already in your favorites.')
    else:
        await send_message(message.channel, f'{coin} is not a valid symbol.')

async def remove_favorite(client, message, args):
    coin = args.upper()
    server_id = str(message.guild.id)
    user_id = str(message.author.id)

    if server_id in db and user_id in db[server_id] and coin in db[server_id][user_id]:
        db[server_id][user_id].remove(coin)
        await send_message(message.channel, f'{coin} removed from your favorites.')
    else:
        await send_message(message.channel, f'{coin} is not in your favorites.')

async def get_favorites(client, message, args):
    server_id = str(message.guild.id)
    user_id = str(message.author.id)

    if server_id in db and user_id in db[server_id] and db[server_id][user_id]:
        favorites = db[server_id][user_id]
        coins_payload = []
        for index, coin in enumerate(favorites, start=1):
            payload = coinMarketCap.getPrice(coin)
            coins_payload.append(payload)
      
        formatted_coins = format_favorite_coins(coins_payload)

        if formatted_coins:
            await send_message(message.channel, f'Your favorite coins:\n{formatted_coins}')
        else:
            await send_message(message.channel, 'You have no favorite coins.')
    else:
        await send_message(message.channel, 'You have no favorite coins.')


async def get_coin(client, message, args):
    symbol = args.strip()
    payload = coinMarketCap.getPrice(symbol)
    print(payload['symbol'])

    if payload is not None:
        await message.channel.send(format_coin_data(payload))
    else:
        await message.channel.send(f"Failed to fetch info. for {symbol}.")