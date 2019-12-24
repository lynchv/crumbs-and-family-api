from FlaskApp import db
from FlaskApp.models.item import Item


class ItemManager(object):
    def __init__(self):
        self.response = {
            "data": None,
            "error": "",
            "warning": "",
        }


    def get_items(self, category):
        print("getting all items with {}".format(category))
        items = Item.query.filter_by(category=category).all()
        self.response["data"] = items


    def create_item(self, new_item):
        print("creating an item with {}".format(new_item))
        item = Item(
            name= new_item["name"],
            category= new_item["category"],
            description= new_item["description"],
            image= new_item["image"],
            price= new_item["price"],
        )
        db.session.add(item)
        db.session.commit()

        
    def update_item(self, item_id, new_item):
        print("updating item {} with {}".format(item_id, new_item))

        
    def delete_item(self, item_id):
        print("deleting item {}".format(item_id))