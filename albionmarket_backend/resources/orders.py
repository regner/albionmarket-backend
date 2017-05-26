

from datetime import datetime

from flask_restful import Resource, abort

from .orders_stats import fetch_item_market_stats
from ..models import MarketOrder, Item


class OrdersV1(Resource):
    def get(self, item_id):
        item = Item.query.get(item_id)

        if item is None:
            abort(404)

        orders = MarketOrder\
            .query\
            .filter(MarketOrder.expire_time > datetime.utcnow())\
            .filter_by(item_id=item_id)\
            .order_by(MarketOrder.price)

        data = {
            'item': {
                'id': item.id,
                'name': item.name,
                'category_id': item.category_id,
                'sub_category_id': item.sub_category_id,
                'tier': item.tier,
            },
            'orders': [{
                'id': x.id,
                'item_id': x.item_id,
                'location_id': x.location_id,
                'quality_level': x.quality_level,
                'enchantment_level': x.enchantment_level,
                'price': x.price,
                'amount': x.amount,
                'expire_time': x.expire_time.isoformat(),
                'ingest_time': x.ingest_time.isoformat(),
                'last_updated': x.last_updated.isoformat(),
            } for x in orders],
            'stats': fetch_item_market_stats(item_id)
        }

        return data, 200
