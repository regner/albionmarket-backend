

from datetime import datetime

from flask_restful import Resource
from sqlalchemy.sql import func

from ..models import MarketOrder


def fetch_buy_or_sell_item_market_stats(item_id, is_buy_order):
    stats = MarketOrder \
        .query \
        .filter(MarketOrder.expire_time > datetime.utcnow()) \
        .filter_by(item_id=item_id, is_buy_order=is_buy_order) \
        .with_entities(
            func.sum(MarketOrder.amount).label('total_volume'),
            func.avg(MarketOrder.price).label('price_average'),
            func.min(MarketOrder.price).label('price_minimum'),
            func.max(MarketOrder.price).label('price_maximum'),
            func.count(MarketOrder.id).label('order_count'),
        ).one()

    return {
        'total_volume': stats.total_volume if stats.total_volume else 0,
        'price_average': round(float(stats.price_average), 2) if stats.price_average else 0,
        'price_minimum': stats.price_minimum if stats.price_minimum else 0,
        'price_maximum': stats.price_maximum if stats.price_maximum else 0,
        'order_count': stats.order_count,
    }


def fetch_item_market_stats(item_id):
    return {
        'buy': fetch_buy_or_sell_item_market_stats(item_id, True),
        'sell': fetch_buy_or_sell_item_market_stats(item_id, False),
    }


class OrdersStatsV1(Resource):
    def get(self, item_id):
        return fetch_item_market_stats(item_id), 200
