

from flask_restful import Resource

from ..extensions import cache
from ..models import Item


class ItemsV1(Resource):
    @cache.cached()
    def get(self):
        items = Item.query
        data = {
            'items': [{
                'id': x.id,
                'name': x.name,
                'category_id': x.category_id,
                'sub_category_id': x.sub_category_id,
                'tier': x.tier,
            } for x in items],
        }

        return data, 200
