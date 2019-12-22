from flask import request
from flask_restplus import Namespace, Resource
from FlaskApp.models.item import Item
from FlaskApp.item_manager import ItemManager

api = Namespace('cats', description='Cats related operations')


@api.route('/add/<type>')
class GetItems(Resource):
    def get(self, type):
        m = ItemManager()
        m.get_items()
        return "test"
