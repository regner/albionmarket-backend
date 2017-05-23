

from flask_restful import Resource, fields, marshal_with

from ..models import Item
from ..extensions import cache

item = {
    'id': fields.String,
    'name': fields.String,
    'category_id': fields.String,
    'sub_category_id': fields.String,
    'tier': fields.Integer,
}

item_list = {
    'items': fields.List(fields.Nested(item)),
}


class ItemsV1(Resource):
    @marshal_with(item_list)
    @cache.cached(timeout=600)
    def get(self):
        items = Item.query

        return {
            'items': items,
        }, 200
