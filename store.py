from email.policy import default

import yaml

import errors
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
            if item_name in prod.name and prod.name not in self._shopping_cart.items:
                searchlst.append(prod)
        searchlst = self._sort_by_hashtag(searchlst)
        return searchlst

    def search_by_hashtag(self, hashtag: str) -> list:
        searchlst = []
        for prod in self.get_items():
            if hashtag in prod.hashtags and prod.name not in self._shopping_cart.items:
                searchlst.append(prod)
        searchlst = self._sort_by_hashtag(searchlst)
        return searchlst

    def add_item(self, item_name: str):
        count = 0
        for item in self._items: # checks how many items name matches item_name
            if item_name in item.name:
                count +=1
        if count == 1: # only one item matches' adds it to shopping cart,
            # add_item raises ItemAlreadyExistsError if needed
            self._shopping_cart.add_item(self._shopping_cart.items(item_name))
        elif count > 1: # multiple items matching, raises TooManyMatchesError
            raise errors.TooManyMatchesError("There are multiple items matching the given name")
        else: # no such item exists
            raise errors.ItemNotExistError("There is no item with the given name")

    def remove_item(self, item_name: str):
        # TODO: Complete
        pass

    def checkout(self) -> int:
        # TODO: Complete
        pass

    def _sort_by_hashtag(self, items_list: list) -> list:
        hashtag_list = [] # building a new hash list
        for item in self._shopping_cart.items: # building list of all hashtags of all items in current shopping cart
            hashtag_list += item.hashtags
        hash_dict = {} # dict for items and their num of matching to hashtag_list
        for item in items_list: # counting matches for each item
            hash_count = 0
            for hashtag in hashtag_list:
                if hashtag in item.hashtags:
                    hash_count += 1
            hash_dict[item] = hash_count # adding to dict
        item_hash_lst = list(hash_dict.items()) # get list of tuples : (item,count)
        item_hash_lst.sort(key=lambda item: item[0].name) # first sort by names, handling equal counters
        item_hash_lst.sort(key=lambda item : item[1]) # sort by counts
        sort_lst = [] # building the sort list
        for item in item_hash_lst: # dict is sort, appends to list by order
            sort_lst.append(item[0])
        return sort_lst