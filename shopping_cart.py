from item import Item
import errors

class ShoppingCart:
    def __init__(self): #constructor
        self.items = {}

    def add_item(self, item: Item):
        if item in self.items: #  item name already exists in the shopping cart
            raise errors.ItemAlreadyExistsError("Item {} already exists".format(str(item))
        else:
            self.items[item.name]= item # add item to shopping cart

    def remove_item(self, item_name: str):
        if item_name not in self.items: # no item with the given name exists
            raise errors.ItemNotExistError("Item {} doesn't exist".format(item_name))
        else:
            del self.items[item_name] # remove item from the shopping cart

    def get_subtotal(self) -> int:
        # TODO: Complete
        pass
