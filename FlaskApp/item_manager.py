from FlaskApp.models.item import Item

class ItemManager(object):
    def get_items(self, item_type):
        print("getting all items with {}".format(item_type))
        pass

    def create_item(self, new_item):
        print("creating an item")
        pass
        
    def update_item(self, new_item):
        print("updating an item")
        pass
        
    def delete_item(self, item_id):
        print("deleting an item")
        pass