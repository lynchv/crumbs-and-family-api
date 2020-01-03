import os, yaml
from flask import abort
from FlaskApp import db
from FlaskApp.models.item import Item



class ItemManager(object):
    def __init__(self):
        file_dir = os.path.dirname(__file__)
        with open(os.path.join(file_dir, "config.yaml")) as f:
            self.cfg = yaml.load(f, Loader=yaml.FullLoader)

        self.response = {
            "data": None,
            "error": "",
            "warning": "",
        }


    def get_items(self, category):
        print("getting all items with {}".format(category))
        if category:
            items = Item.query.filter_by(category=category).all()
        else:
            items = Item.query.filter_by().all()
        self.response["data"] = [i.to_json() for i in items]


    def create_item(self, new_item):
        print("creating an item with {}".format(new_item))
        self.__validate_item(new_item)
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
        old_item =  Item.query.filter_by(item_id=item_id).one_or_none()
        if not item:
            abort(400, "Item can not be found")
        self.__validate_item(new_item)
        old_item.image = new_item['image'] if "image" in new_item else old_item.image
        old_item.name = new_item['name']
        old_item.category = new_item['category']
        old_item.description = new_item['description']
        old_item.price = new_item['price']
        db.session.commit()
        

    def delete_item(self, item_id):
        print("deleting item {}".format(item_id))
        item =  Item.query.filter_by(item_id=item_id).one_or_none()
        if not item:
            abort(400, "Item can not be found")
        db.session.delete(item)
        db.session.commit()

    def __validate_item(self, item):
        if item["category"] not in self.cfg["supported_category"]:
            err_msg = "Item type '{}' is not supported".format(item['category'])
            abort(400, err_msg)

        if len(item["description"]) > 2048:
            err_msg = "Description can not be longer then 2048 characters"
            abort(400, err_msg)

