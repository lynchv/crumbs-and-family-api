from flask import request
from flask_restplus import Namespace, Resource, fields
from FlaskApp.models.item import Item
from FlaskApp.item_manager import ItemManager

api = Namespace('item', description='Namespace to interact with items.')

item_model = api.model('Model', {
    'item_id': fields.Integer(required=False),
    'name': fields.String(required=True),
    'category': fields.String(required=True),
    'description': fields.String(required=True),
    'image': fields.String(required=False),
    'price': fields.Integer(required=True),
})

@api.route('/create')
class CreateItem(Resource):
    @api.expect(item_model)
    def post(self):
        m = ItemManager()
        m.create_item(request.json) # content type: application/json 
        return m.response


@api.route('/<category>')
class GetItems(Resource):
    def get(self, category):
        m = ItemManager()
        m.get_items(category)
        return m.response


@api.route('/modify/<item_id>')
class ModifyItem(Resource):
    def put(self, item_id):
        m = ItemManager()
        m.update_item(item_id, request.json)
        return m.response

    
    def delete(self, item_id):
        m = ItemManager()
        m.delete_item(item_id)
        return m.response