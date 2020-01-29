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
            "message": "",
        }


    def get_items(self, category = False):
        print("getting all items with {}".format(category))
        if category:
            items = Item.query.filter_by(category=category).all()
        else:
            items = Item.query.all()
        self.response["data"] = [i.to_json() for i in items]

    
    def get_all_categories(self):
        self.response['data'] = self.cfg["supported_category"]


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
        

    def delete_item(self, item_id):
        print("deleting item {}".format(item_id))
        item =  Item.query.filter_by(item_id=item_id).one_or_none()
        if not item:
            abort(400, "Item can not be found")
        db.session.delete(item)
        db.session.commit()
        self.response['data'] = True


    def __validate_item(self, item):
        if item["category"] not in self.cfg["supported_category"]:
            err_msg = "Item category '{}' is not supported".format(item['category'])
            abort(400, err_msg)

        if len(item["description"]) > 2048:
            err_msg = "Description can not be longer then 2048 characters"
            abort(400, err_msg)

