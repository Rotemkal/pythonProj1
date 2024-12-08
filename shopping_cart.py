from item import Item
import errors

class ShoppingCart:
    def __init__(self): #constructor
        self.items = {}

    def add_item(self, item: Item):
        if item in self.items:
            raise errors.ItemAlreadyExistsError("Item {} already exists".format(item))
        else:
            self.items[item.name]= item

    def remove_item(self, item_name: str):
        # TODO: Complete
        pass

    def get_subtotal(self) -> int:
        # TODO: Complete
        pass
