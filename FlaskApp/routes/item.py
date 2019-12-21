from flask_restplus import Namespace, Resource
from FlaskApp.models.item import Item

api = Namespace('cats', description='Cats related operations')


@api.route('/')
class CatList(Resource):
    def get(self):
        print("here")
        print(Item.query.all())
        return "test"
