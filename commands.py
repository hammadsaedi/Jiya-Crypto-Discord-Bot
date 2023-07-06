from coin_utils import *

command_mappings = {
    '$get': get_coin,
    '$add': add_favorite,
    '$remove': remove_favorite,
    '$favorites': get_favorites,
    '$buy': buy,
    '$sell': sell,
    '$portfolio': get_portfolio,
    '$transfer': transfer,
    '$check': check_portfolio,
    '$help': help_command,
}
