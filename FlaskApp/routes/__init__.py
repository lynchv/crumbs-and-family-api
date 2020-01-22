from flask_restplus import Api

from .item import api as item
from .user import api as user

api = Api(
    title='My Title',
    version='1.0',
    description='A description',
)

api.add_namespace(item)
api.add_namespace(user)