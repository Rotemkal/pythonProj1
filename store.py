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
        """Return value: a sorted list of all the items
         that match the search term"""
        search_lst = []
        for prod in self.get_items(): # building search_lst, adds relevant product
            if item_name in prod.name and prod.name not in self._shopping_cart.items:
                search_lst.append(prod)
        search_lst = self._sort_by_hashtag(search_lst) # sorts search_lst by using _sort_by_hashtag
        return search_lst

    def search_by_hashtag(self, hashtag: str) -> list:
        """Return a sorted list of all the items
         matching the search criterion"""
        search_lst = []
        for prod in self.get_items(): # building search_lst, adds relevant product
            if hashtag in prod.hashtags and prod.name not in self._shopping_cart.items:
                search_lst.append(prod)
        search_lst = self._sort_by_hashtag(search_lst) # sorts search_lst by using _sort_by_hashtag
        return search_lst

    def add_item(self, item_name: str):
        """Adds an item with the given name to the customer’s shopping cart,
        if no such item exists, raises ItemNotExistError, If the given item is
        already in the shopping cart, raises ItemAlreadyExistsError"""
        count = 0
        curr = None
        for item in self._items: # checks how many items name matches item_name
            if item_name in item.name:
                count += 1
                curr = item
        if count == 1: # one item matches, adds it to shopping cart,
            # add_item raises ItemAlreadyExistsError if needed
            self._shopping_cart.add_item(curr)
        elif count > 1: # multiple items matching, raises TooManyMatchesError
            raise errors.TooManyMatchesError("There are multiple items matching the given name")
        else: # no such item exists
            raise errors.ItemNotExistError("There is no item with the given name")

    def remove_item(self, item_name: str):
        """Removes an item with the given name from the customer’s
         shopping cart, if no such item exists, raises ItemNotExistError,
         If there are multiple items matching the given name, raises TooManyMatchesError"""
        count = 0
        curr = None
        for item in self._items: # checks how many items name matches item_name
            if item_name in item.name:
                count += 1
                curr = item.name # saving the item to add if relevant
        if count == 1: # one item matches, adds it to shopping cart,
            # remove_item raises ItemNotExistError if needed
            self._shopping_cart.remove_item(curr)
        elif count > 1: # multiple items matching, raises TooManyMatchesError
            raise errors.TooManyMatchesError("There are multiple items matching the given name")
        else: # no such item exists
            raise errors.ItemNotExistError("There is no item with the given name")


    def checkout(self) -> int:
        """Returns the total price of all the items
         in the costumer’s shopping cart"""
        return self._shopping_cart.get_subtotal()

    def _sort_by_hashtag(self, items_list: list) -> list:
        hashtag_list = [] # building a new hash list
        for item in self._shopping_cart.items.values(): # building list of all hashtags of all items in current shopping cart
            hashtag_list += item.hashtags
        hash_dict = {} # dict for items and their num of matching to hashtag_list
        for item in items_list: # counting matches for each item
            hash_count = 0
            for hashtag in hashtag_list:
                if hashtag in item.hashtags:
                    hash_count += 1
            hash_dict[item] = hash_count # adding to dict
        item_hash_lst = list(hash_dict.items()) # get list of tuples : (item,count)
        item_hash_lst.sort(key=lambda item : item[0].name) # first sort by names, handling equal counters
        item_hash_lst.sort(key=lambda item : item[1]) # sort by counts
        sort_lst = [] # building the sort list
        for item in item_hash_lst: # dict is sort, appends to list by order
            sort_lst.append(item[0])
        return sort_lst