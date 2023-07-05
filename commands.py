from coin_utils import *

command_mappings = {
    '$get': get_coin,
    '$commands': lambda client, message, args: send_message(message.channel, 'To fetch price from CoinMarketCap: get <coin_symbol>'),
    '$authors': lambda client, message, args: send_message(message.channel, 'FA21-BCS-020 Fasiha Arshad\nFA21-BCS-023 Hammad Saeedi'),
    '$add': add_favorite,
    '$remove': remove_favorite,
    '$favorites': get_favorites,
}
