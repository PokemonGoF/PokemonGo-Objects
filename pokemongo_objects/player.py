class Player:
    def __init__(self, response_dict):
        player_handle = response_dict['response']['GET_PLAYER']
        self.username = player_handle['player_data']['username']

        self.pokecoins = 0
        self.stardust = 0
        currencies = player_handle['player_data']['currencies']
        for currency in currencies:
            if currency['name'].lower() == 'pokecoin':
                if 'amount' in currency:
                    self.pokecoins = currency['amount']
            elif currency['name'].lower() == 'stardust':
                if 'amount' in currency:
                    self.stardust = currency['amount']

        self.max_item_storage = player_handle['player_data']['max_item_storage']
        self.max_pokemon_storage = player_handle['player_data']['max_pokemon_storage']
