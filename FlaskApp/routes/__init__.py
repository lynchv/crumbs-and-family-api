from flask_restplus import Api

from .item import api as item

api = Api(
    title='My Title',
    version='1.0',
    description='A description',
)

api.add_namespace(item)