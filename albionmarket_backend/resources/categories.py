

from flask_restful import Resource, fields

from ..models import Category, SubCategory
from ..extensions import cache


category = {
    'id': fields.String,
    'name': fields.String,
}

category_list = {
    'categories': fields.List(fields.Nested(category)),
    'sub_categories': fields.List(fields.Nested(category)),
}


class CategoriesV1(Resource):
    @cache.cached()
    def get(self):
        data = {
            'categories': [{
                'id': x.id,
                'name': x.name,
            } for x in Category.query],
            'sub_categories': [{
                'id': x.id,
                'name': x.name,
            } for x in SubCategory.query],
        }

        return data, 200
