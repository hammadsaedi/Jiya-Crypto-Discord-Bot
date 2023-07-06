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
        db[server_id][user_id] = {
            "favorites": [],
            "portfolio": {}
        }

    is_valid = await check_valid_coin(coin)

    if is_valid:
        if coin not in db[server_id][user_id]["favorites"]:
            db[server_id][user_id]["favorites"].append(coin)
            await send_message(message.channel, f'{coin} added to your favorites.')
        else:
            await send_message(message.channel, f'{coin} is already in your favorites.')
    else:
        await send_message(message.channel, f'{coin} is not a valid symbol.')


async def remove_favorite(client, message, args):
    coin = args.upper()
    server_id = str(message.guild.id)
    user_id = str(message.author.id)

    if server_id in db and user_id in db[server_id] and coin in db[server_id][user_id]["favorites"]:
        db[server_id][user_id]["favorites"].remove(coin)
        await send_message(message.channel, f'{coin} removed from your favorites.')
    else:
        await send_message(message.channel, f'{coin} is not in your favorites.')


async def get_favorites(client, message, args):
    server_id = str(message.guild.id)
    user_id = str(message.author.id)

    if server_id in db and user_id in db[server_id] and db[server_id][user_id]["favorites"]:
        favorites = db[server_id][user_id]["favorites"]
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

    if payload is not None:
        await message.channel.send(format_coin_data(payload))
    else:
        await message.channel.send(f"Failed to fetch info. for {symbol}.")


async def buy(client, message, args):
    params = args.split()
    if len(params) == 3:
        coin = params[0].upper()
        quantity = float(params[1])
        price = params[2]

        if price.lower() == 'current':
            payload = coinMarketCap.getPrice(coin)
            if not payload:
                await send_message(message.channel, f"Failed to fetch price for {coin}.")
                return

            price = round_price(payload['quote']['USD']['price'])
        else:
            price = round_price(float(price))

        server_id = str(message.guild.id)
        user_id = str(message.author.id)

        if server_id not in db:
            db[server_id] = {}

        if user_id not in db[server_id]:
            db[server_id][user_id] = {
                "favorites": [],
                "portfolio": {}
            }

        is_valid = await check_valid_coin(coin)

        if is_valid:
            user_portfolio = db[server_id][user_id]["portfolio"]
            if coin not in user_portfolio:
                user_portfolio[coin] = [
                  {
                    'quantity': quantity,
                    'price': price
                  }
                ]
            else:
                holding = {
                  'quantity': quantity,
                  'price': price
                }
                user_portfolio[coin].append(holding)
            
            total_value = quantity * price

            print(db[server_id][user_id]["portfolio"][coin])
            await send_message(message.channel, f"You have bought {quantity} {coin} at a price of {price} USD. "
                                                 f"Total value: {total_value} USD")
        else:
            await send_message(message.channel, f"{coin} is not a valid symbol.")
    else:
        await send_message(message.channel, "Invalid command format. Usage: $buy <coin_symbol> <quantity> <price>")


async def sell(client, message, args):
    params = args.split()
    if len(params) == 3:
        coin = params[0].upper()
        quantity = params[1]
        price = params[2]

        if price.lower() == 'current':
            payload = coinMarketCap.getPrice(coin)
            if not payload:
                await send_message(message.channel, f"Failed to fetch price for {coin}.")
                return

            price = round_price(payload['quote']['USD']['price'])

        server_id = str(message.guild.id)
        user_id = str(message.author.id)

        if server_id in db and user_id in db[server_id]:
            user_portfolio = db[server_id][user_id]["portfolio"]
            if coin in user_portfolio:
                coin_holdings = user_portfolio[coin]
                if coin_holdings:
                    total_quantity = 0
                    total_value = 0

                    for holding in coin_holdings:
                        total_quantity += holding['quantity']
                        total_value += holding['quantity'] * holding['price']

                    if total_quantity >= float(quantity):
                        remaining_quantity = float(quantity)
                        remaining_value = remaining_quantity * float(price)
                        updated_holdings = []

                        for holding in coin_holdings:
                            if holding['quantity'] <= remaining_quantity:
                                remaining_quantity -= holding['quantity']
                            else:
                                holding['quantity'] -= remaining_quantity
                                remaining_value -= remaining_quantity * holding['price']
                                updated_holdings.append(holding)

                        if updated_holdings:
                            user_portfolio[coin] = updated_holdings
                        else:
                            del user_portfolio[coin]

                        await send_message(message.channel, f"You have sold {quantity} {coin} at a price of {price} USD. "
                                                             f"Total value: {remaining_value} USD")
                    else:
                        await send_message(message.channel, f"You do not have enough {coin} to sell.")
                else:
                    await send_message(message.channel, f"You do not own any {coin}.")
            else:
                await send_message(message.channel, f"You do not own {coin}.")
        else:
            await send_message(message.channel, "You do not have any coins in your portfolio.")
    else:
        await send_message(message.channel, "Invalid command format. Usage: $sell <coin_symbol> <quantity> <price>")


def get_user_id_from_mention(mention):
    if mention.startswith("<@") and mention.endswith(">"):
        user_id = mention[2:-1]
        if user_id.startswith("!"):
            user_id = user_id[1:]
        return user_id
    return None


async def transfer(client, message, args):
    params = args.split()
    if len(params) == 3:
        quantity = float(params[0])
        coin = params[1].upper()
        recipient_mention = params[2]

        # Fetch recipient user ID from the mention
        recipient_id = get_user_id_from_mention(recipient_mention)
        if not recipient_id:
            await send_message(message.channel, 'Invalid recipient. Please mention a valid user.')
            return

        server_id = str(message.guild.id)
        user_id = str(message.author.id)

        if server_id in db and user_id in db[server_id]:
            user_portfolio = db[server_id][user_id]["portfolio"]
            if coin in user_portfolio:
                coin_holdings = user_portfolio[coin]
                if coin_holdings:
                    total_quantity = 0
                    for holding in coin_holdings:
                        total_quantity += holding['quantity']

                    if total_quantity >= quantity:
                        remaining_quantity = quantity
                        transferred_holdings = []
                        for holding in coin_holdings:
                            if holding['quantity'] <= remaining_quantity:
                                remaining_quantity -= holding['quantity']
                            else:
                                transferred_quantity = remaining_quantity
                                holding['quantity'] -= remaining_quantity
                                transferred_holdings.append({
                                    'quantity': transferred_quantity,
                                    'price': holding['price']
                                })
                                break

                        if remaining_quantity == 0:
                            del user_portfolio[coin]
                        else:
                            user_portfolio[coin] = transferred_holdings

                        # Add transferred coins to recipient's portfolio
                        if server_id not in db:
                            db[server_id] = {}
                        if recipient_id not in db[server_id]:
                            db[server_id][recipient_id] = {
                                "favorites": [],
                                "portfolio": {}
                            }

                        recipient_portfolio = db[server_id][recipient_id]["portfolio"]
                        if coin not in recipient_portfolio:
                            recipient_portfolio[coin] = transferred_holdings
                        else:
                            recipient_portfolio[coin].extend(transferred_holdings)

                        await send_message(message.channel, f"You have transferred {quantity} {coin} to {recipient_mention}.")
                    else:
                        await send_message(message.channel, f"You do not have enough {coin} to transfer.")
                else:
                    await send_message(message.channel, f"You do not own any {coin}.")
            else:
                await send_message(message.channel, f"You do not own {coin}.")
        else:
            await send_message(message.channel, "You do not have any coins in your portfolio.")
    else:
        await send_message(message.channel, "Invalid command format. Usage: $transfer <quantity> <coin_symbol> <recipient>")


async def create_portfolio_response(server_id, user_id):
    if server_id in db and user_id in db[server_id]:
        user_portfolio = db[server_id][user_id]["portfolio"]
        if user_portfolio:
            portfolio_summary = []
            total_invested = 0
            total_current_value = 0
            total_profit_loss = 0

            for coin, holdings in user_portfolio.items():
                total_quantity = 0
                total_invested_per_coin = 0
                current_value_per_coin = 0

                for holding in holdings:
                    total_quantity += float(holding['quantity'])
                    total_invested_per_coin += round_price(holding['quantity'] * holding['price'])

                # Fetch the current price of the coin
                payload = coinMarketCap.getPrice(coin)
                if payload:
                    current_price = payload['quote']['USD']['price']
                    current_value_per_coin = round_price(total_quantity * current_price)

                profit_loss_per_coin = current_value_per_coin - total_invested_per_coin
                portfolio_summary.append(f"{coin}: \n Quantity - {total_quantity}\n "
                                         f"Total Invested - {total_invested_per_coin} USD\n "
                                         f"Current Value - {current_value_per_coin} USD\n "
                                         f"Profit/Loss - {profit_loss_per_coin} USD \n \n")

                total_invested += total_invested_per_coin
                total_current_value += current_value_per_coin
                total_profit_loss += profit_loss_per_coin

            portfolio_info = "\n".join(portfolio_summary)
            return portfolio_info, total_invested, total_current_value, total_profit_loss
    return None, 0, 0, 0


async def get_portfolio(client, message, args):
    server_id = str(message.guild.id)
    user_id = str(message.author.id)

    portfolio_info, total_invested, total_current_value, total_profit_loss = await create_portfolio_response(server_id, user_id)
    if portfolio_info:
        portfolio_message = f"Your portfolio:\n\n{portfolio_info}\n"
        portfolio_message += f"Total Invested: {total_invested} USD\n"
        portfolio_message += f"Total Current Value: {total_current_value} USD\n"
        portfolio_message += f"Overall Profit/Loss: {total_profit_loss} USD"
        await send_message(message.channel, portfolio_message)
    else:
        await send_message(message.channel, "Your portfolio is empty.")


async def check_portfolio(client, message, args):
    # Check if the user invoking the command is an admin
    if not message.author.guild_permissions.administrator:
        await send_message(message.channel, "You don't have permission to check the portfolio.")
        return

    user_mention = args.strip()
    user_id = get_user_id_from_mention(user_mention)

    if not user_id:
        await send_message(message.channel, 'Invalid user mention. Please mention a valid user.')
        return

    server_id = str(message.guild.id)

    portfolio_info, total_invested, total_current_value, total_profit_loss = await create_portfolio_response(server_id, user_id)
    if portfolio_info:
        portfolio_message = f"Portfolio of {user_mention}:\n\n{portfolio_info}\n"
        portfolio_message += f"Total Invested: {total_invested} USD\n"
        portfolio_message += f"Total Current Value: {total_current_value} USD\n"
        portfolio_message += f"Overall Profit/Loss: {total_profit_loss} USD"
        await send_message(message.channel, portfolio_message)
    else:
        await send_message(message.channel, f"{user_mention} does not have any coins in their portfolio.")


async def help_command(client, message, args):
  help_message = """
  ----Bot Commands----
  
  ---Get Price---
  $get <coin_symbol>
  Get information about a specific coin.

  
  ---Favorites---
  $add <coin_symbol>
  Add a coin to your favorites.
  
  $remove <coin_symbol>
  Remove a coin from your favorites.
  
  $favorites
  Get your favorite coins.
  
  ---Portfolio---
  $buy <coin_symbol> <quantity> <price> 
  Buy a specific quantity of a coin at a given price.
  
  $sell <coin_symbol> <quantity> <price>
  Sell a specific quantity of a coin at a given price.
  
  $transfer <quantity> <coin_symbol> <recipient_mention>
  Transfer a specific quantity of a coin to another user.
  
  $portfolio: 
  Get your portfolio
  
  $check <user>
  Get portfolio of any user (Admin Only)
  """

  await send_message(message.channel, help_message)
