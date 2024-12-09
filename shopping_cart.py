from item import Item
import errors

class ShoppingCart:
    def __init__(self): #constructor
        """initialize the shopping cart instance,
        a dictionary to store the current items in the shopping cart"""
        self.items = {}

    def add_item(self, item: Item):
        """Adds an item to the shopping cart,
        raises ItemAlreadyExistsError if item is already exist"""
        if item.name in self.items: #  name already exists in the shopping cart
            raise errors.ItemAlreadyExistsError(
                "Item {} already exists".format(item.name))
        else:
            self.items[item.name] = item  # add item to shopping cart

    def remove_item(self, item_name: str):
        """Removes an item from the shopping cart,
        raises ItemNotExistError if item does not exist"""
        if item_name not in self.items: # no item with the given name exists
            raise errors.ItemNotExistError(
                "Item {} doesn't exist".format(item_name))
        else:
            del self.items[item_name] # remove item from the shopping cart

    def get_subtotal(self) -> int:
        """Returns the subtotal of the items in the shopping cart"""
        subtotal = 0
        for item in self.items.values():
            subtotal += item.price
        return subtotal
