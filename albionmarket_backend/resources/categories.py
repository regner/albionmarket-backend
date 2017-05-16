

from flask_restful import Resource, fields, marshal_with

from ..models import Category, SubCategory


category = {
    'id': fields.String,
    'name': fields.String,
}

category_list = {
    'categories': fields.List(fields.Nested(category)),
    'sub_categories': fields.List(fields.Nested(category)),
}


class CategoriesV1(Resource):
    @marshal_with(category_list)
    def get(self):
        return {
            'categories': Category.query,
            'sub_categories': SubCategory.query,
        }, 200
