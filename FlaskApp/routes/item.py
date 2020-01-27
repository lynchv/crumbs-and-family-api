from flask import request, abort
from flask_login import login_required, current_user
from flask_restplus import Namespace, Resource, fields
from FlaskApp.models.item import Item
from FlaskApp.item_manager import ItemManager

api = Namespace('item', description='Namespace to interact with items.')

item_model = api.model('Model', {
    'item_id': fields.Integer(required=False),
    'name': fields.String(required=True),
    'category': fields.String(required=True),
    'description': fields.String(required=True),
    'image': fields.String(required=True),
    'price': fields.Integer(required=True),
})


@api.route('/categories')
class GetItemGroup(Resource):
    def get(self):
        m = ItemManager()
        m.get_all_categories()
        return m.response


@api.route('/<category>')
class GetItemGroup(Resource):
    def get(self, category):
        m = ItemManager()
        m.get_items(category)
        return m.response


@api.route('/')
class CreateOrGetItem(Resource):
    def get(self):
        m = ItemManager()
        m.get_items()
        return m.response

    @api.expect(item_model)
    @login_required
    def post(self):
        m = ItemManager()
        
        if current_user.is_admin:
            m.create_item(request.json)
        else:
            abort(403, "Only Website admistrator can modify items")
        
        return m.response


@api.route('/<item_id>')
class ModifyItem(Resource):
    @login_required    
    def delete(self, item_id):
        m = ItemManager()
        
        if current_user.is_admin:
            m.delete_item(item_id)
        else:
            abort(403, "Only Website admistrator can modify items")
        
        return m.response