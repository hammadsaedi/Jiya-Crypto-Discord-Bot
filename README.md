# Jiya - Cryptocurrency Discord Bot

Jiya is a Discord bot designed to perform various cryptocurrency-related tasks, including retrieving coin information, managing favorites, buying and selling coins, tracking portfolios, and facilitating transfers between users. The bot utilizes the Discord.py library to interact with the Discord platform and integrates with the CoinMarketCap API to fetch real-time cryptocurrency data.

## Features

- *Retrieve Coin Information*: Users can retrieve detailed information about cryptocurrencies, such as current price, market cap, and trading volume, using the bot's commands.

- *Manage Favorite Cryptocurrencies*: Jiya allows users to create and manage a list of their favorite cryptocurrencies, making it easier to keep track of coins of interest.

- *Simulate Buying and Selling*: The bot provides a simulated buying and selling feature, enabling users to specify the coin, quantity, and price to assess potential outcomes.

- *Track and Manage User Portfolios*: Jiya enables users to track and manage their cryptocurrency portfolios, providing an overview of their holdings, including the quantity and value of each coin.

- *Transfer Cryptocurrencies*: Users can transfer cryptocurrencies to other users within the Discord server, facilitating seamless exchanges between members.

Jiya simplifies cryptocurrency-related tasks within Discord communities, offering valuable insights and tools for managing digital assets.


## Requirements

- Python 3.7 or higher
- Replit (for running the bot)


## Dependencies

The project utilizes the following dependencies:

- Discord.py
- Flask
- CoinMarketCap
- other dependencies listed in `pyproject.toml`



## Installation

To run the Jiya bot, follow these steps:

1. Click on the "Create Repl" button from the sidebar.
2. In the menu to create a new repl, press the "Import from GitHub" button in the top-right corner.
3. Copy the URL of GitHub repository and paste it into the text field.
4. Press the "Import" button.
5. Ensure your Replit project is using Python 3.7 or higher.
6. Set up the environment variables:
   - In Replit, navigate to the "Secrets" tab in the left sidebar.
   - Add a new secret with the key `BOT_TOKEN` and the value being your actual Discord bot token.
   - Add a new secret with the key `CMC_TOKEN` and the value being your actual CoinMarketCap api key.
7. Start the bot:
   - Open the `main.py` file.
   - Click the "Run" button in Replit to start the bot.



## Usage

To interact with the Jiya bot, use the following commands in a Discord channel where the bot is present:

- *`$get <coin_symbol>`*: Retrieves detailed information about the specified cryptocurrency.

   Example: `$get BTC`

   This command will retrieve information such as the current price, market cap, and trading volume of Bitcoin (BTC).

- *`$add <coin_symbol>`*: Adds the specified cryptocurrency to your favorites list.

   Example: `$add ETH`

   This command will add Ethereum (ETH) to your list of favorite cryptocurrencies.

- *`$remove <coin_symbol>`*: Removes the specified cryptocurrency from your favorites list.

   Example: `$remove BTC`

   This command will remove Bitcoin (BTC) from your list of favorite cryptocurrencies.

- *`$favorites`*: Retrieves your favorite cryptocurrencies.

   Example: `$favorites`

   This command will display a list of your favorite cryptocurrencies along with their current prices.

- *`$buy <coin_symbol> <quantity> <price>`*: Simulates buying a certain quantity of a cryptocurrency at a specified price.

   Example: `$buy BTC 1 current`

   This command will simulate buying 1 Bitcoin (BTC) at the current market price.

- *`$sell <coin_symbol> <quantity> <price>`*: Simulates selling a certain quantity of a cryptocurrency at a specified price.

   Example: `$sell ETH 2 500`

   This command will simulate selling 2 Ethereum (ETH) at a price of $500 each.

- *`$portfolio`*: Retrieves your cryptocurrency portfolio.

   Example: `$portfolio`

   This command will display your current cryptocurrency portfolio, including the coins you own and their respective quantities.

- *`$transfer <quantity> <coin_symbol> <recipient_mention>`*: Transfers a specified quantity of a cryptocurrency to another user.

   Example: `$transfer 0.5 BTC @username`

   This command will transfer 0.5 Bitcoin (BTC) to the user mentioned in the command.

Please note that for commands requiring additional parameters (such as quantity and price), make sure to provide the correct values. Additionally, coin symbols should be entered in uppercase letters.



## API Reference

The Jiya bot does not expose a public API. However, it utilizes the following internal methods for its functionality.

### CoinMarketCap API Integration

#### `get_price(coin_symbol)`

Retrieves the current price of a specific cryptocurrency from the CoinMarketCap API.

- Parameters:
  - `coin_symbol`: The symbol or ticker of the cryptocurrency.

#### `get_market_data(coin_symbol)`

Retrieves detailed market data for a specific cryptocurrency from the CoinMarketCap API.

- Parameters:
  - `coin_symbol`: The symbol or ticker of the cryptocurrency.

### Favorites Management

#### `add_favorite(coin_symbol)`

Adds a cryptocurrency to the user's favorites list.

- Parameters:
  - `coin_symbol`: The symbol or ticker of the cryptocurrency.

#### `remove_favorite(coin_symbol)`

Removes a cryptocurrency from the user's favorites list.

- Parameters:
  - `coin_symbol`: The symbol or ticker of the cryptocurrency.

### Portfolio Management

#### `get_portfolio()`

Retrieves the user's cryptocurrency portfolio.

### Trading Simulation

#### `buy_coin(coin_symbol, quantity, price)`

Simulates buying a specific quantity of a cryptocurrency at a specified price.

- Parameters:
  - `coin_symbol`: The symbol or ticker of the cryptocurrency.
  - `quantity`: The quantity to buy.
  - `price`: The price at which to buy.

#### `sell_coin(coin_symbol, quantity, price)`

Simulates selling a specific quantity of a cryptocurrency at a specified price.

- Parameters:
  - `coin_symbol`: The symbol or ticker of the cryptocurrency.
  - `quantity`: The quantity to sell.
  - `price`: The price at which to sell.

### Transfer of Cryptocurrency

#### `transfer_coin(quantity, coin_symbol, recipient_mention)`

Transfers a specified quantity of a cryptocurrency to another user.

- Parameters:
  - `quantity`: The quantity to transfer.
  - `coin_symbol`: The symbol or ticker of the cryptocurrency.
  - `recipient_mention`: The mention of the recipient user.


## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.


## Authors

- [@hammadsaeedi](https://www.github.com/hammadsaeedi)
- [@fasiiha](https://www.github.com/fasiiha)

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Acknowledgements

- [Discord.py](https://discordpy.readthedocs.io/): Python library for creating Discord bots.
- [CoinMarketCap API](https://coinmarketcap.com/api/): API for retrieving cryptocurrency data.



## Environment Variables

To run this project, you will need to add the following environment variables. In Replit, navigate to the "Secrets" tab in the left sidebar.
- `BOT_TOKEN` Discord Bot Token
- `CMC_TOKEN` CoinMarketCap API Key.


## Demo

Insert gif or link to demo
