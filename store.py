import yaml

from item import Item
from shopping_cart import ShoppingCart

class Store:
    def __init__(self, path):
        with open(path) as inventory:
            items_raw = yaml.load(inventory, Loader=yaml.FullLoader)['items']
        self._items = self._convert_to_item_objects(items_raw)
        self._shopping_cart = ShoppingCart()

    @staticmethod
    def _convert_to_item_objects(items_raw):
        return [Item(item['name'],
                     int(item['price']),
                     item['hashtags'],
                     item['description'])
                for item in items_raw]

    def get_items(self) -> list:
        return self._items

    def search_by_name(self, item_name: str) -> list:
        searchlst = []
        for prod in self.get_items():
            if item_name in prod.name and item_name not in self._shopping_cart.items:
                searchlst.append(prod)
        searchlst.sort(key=lambda prod : prod.name)
        return searchlst

    def search_by_hashtag(self, hashtag: str) -> list:
        # TODO: Complete
        pass

    def add_item(self, item_name: str):
        # TODO: Complete
        pass

    def remove_item(self, item_name: str):
        # TODO: Complete
        pass

    def checkout(self) -> int:
        # TODO: Complete
        pass

    def _sort_by_hashtag(self, items_list: list) -> list:
        hashtag_list = []
        for item in self._shopping_cart.items:
            hashtag_list += item.hashtags
        hash_dict = {}
        for item in items_list:
            hash_count = 0
            for hashtag in hashtag_list:
                if hashtag in item.hashtags:
                    hash_count += 1
        item_hash_lst = list(hash_dict.items()) # get list of tuples : (item,count)
        item_hash_lst.sort(key=lambda item : item[1])
        sort_lst = []
        for item in item_hash_lst :
            sort_lst.append(item[0])
        return sort_lst