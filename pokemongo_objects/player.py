class Player:
    def __init__(self, response_dict):
        player_data = response_dict['response']['GET_PLAYER']['player_data']

        self._processProfile(player_data)
        self._processCurrencies(player_data['currencies'])
        self._processStorage(player_data)

    def _processProfile(self, player_data):
        self.username = player_data['username']

    def _processCurrencies(self, currencies):
        self.pokecoins = 0
        self.stardust = 0
        for currency in currencies:
            if currency['name'].lower() == 'pokecoin':
                if 'amount' in currency:
                    self.pokecoins = currency['amount']
            elif currency['name'].lower() == 'stardust':
                if 'amount' in currency:
                    self.stardust = currency['amount']

    def _processStorage(self, player_data):
        self.max_item_storage = player_data['max_item_storage']
        self.max_pokemon_storage = player_data['max_pokemon_storage']
