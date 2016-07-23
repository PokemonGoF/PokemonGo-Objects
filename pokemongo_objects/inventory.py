from pieces.item import Item

from pieces.pokemon import Pokemon


class Inventory:
    def __init__(self, response_dict):
        self.items = {}
        self.pokemon = {}

        for entry in response_dict['responses']['GET_INVENTORY']['inventory_delta']['inventory_items']:
            if 'inventory_item_data' in entry:
                entry = entry['inventory_item_data']
                if 'pokemon_data' in entry:
                    self.pokemon[entry['pokemon_data']['pokemon_id']] = Pokemon(entry['pokemon_data'])
                elif 'item' in entry:
                    self.items[entry['item']['item_id']] = Item(entry['item'])
                else:
                    continue  # ignore other types yet
            else:
                raise RuntimeError('Invalid inventory structure')
