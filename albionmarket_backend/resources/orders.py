

from datetime import datetime

from flask_restful import Resource, abort

from .orders_stats import fetch_item_market_stats
from ..models import MarketOrder, Item


def fetch_item_orders(item_id, is_buy_order):
    if is_buy_order:
        order_by = MarketOrder.price.desc()

    else:
        order_by = MarketOrder.price

    orders = MarketOrder \
        .query \
        .filter(MarketOrder.expire_time > datetime.utcnow()) \
        .filter_by(item_id=item_id, is_buy_order=is_buy_order) \
        .order_by(order_by)

    return [{
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
        'is_buy_order': x.is_buy_order,
    } for x in orders]


class OrdersV1(Resource):
    def get(self, item_id):
        item = Item.query.get(item_id)

        if item is None:
            abort(404)

        data = {
            'item': {
                'id': item.id,
                'name': item.name,
                'category_id': item.category_id,
                'category_name': item.category.name,
                'sub_category_id': item.sub_category_id,
                'sub_category_name': item.sub_category.name,
                'tier': item.tier,
            },
            'orders': {
                'buy': fetch_item_orders(item_id, True),
                'sell': fetch_item_orders(item_id, False),
            },
            'stats': fetch_item_market_stats(item_id)
        }

        return data, 200
