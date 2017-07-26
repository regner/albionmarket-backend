

from flask_restful import Resource
from sqlalchemy import not_

from .orders_stats import fetch_item_market_stats
from ..models import Item


class OrdersResourcesV1(Resource):
    def get(self):
        resources = Item.query.filter(not_(Item.id.like('%_LEVEL%'))).filter_by(category_id='resources')

        results = []

        for item in resources:
            stats = {
                'stats': fetch_item_market_stats(item.id),
                'item': {
                    'id': item.id,
                    'name': item.name,
                    'category_id': item.category_id,
                    'category_name': item.category.name,
                    'sub_category_id': item.sub_category_id,
                    'sub_category_name': item.sub_category.name,
                    'tier': item.tier,
                },
            }

            results.append(stats)

        data = {
            'resources': results
        }

        return data, 200
