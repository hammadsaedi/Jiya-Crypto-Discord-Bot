
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
