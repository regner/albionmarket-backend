

from datetime import datetime

from sqlalchemy.sql import func
from flask_restful import Resource, fields, marshal_with

from ..models import MarketOrder


order = {
    'id': fields.Integer,
    'item_id': fields.String,
    'location_id': fields.Integer,
    'tier': fields.Integer,
    'quality_level': fields.Integer,
    'enchantment_level': fields.Integer,
    'price': fields.Integer,
    'amount': fields.Integer,
    'expire_time': fields.DateTime(dt_format='iso8601'),
    'ingest_time': fields.DateTime(dt_format='iso8601'),
    'last_updated': fields.DateTime(dt_format='iso8601'),
}

order_stats = {
    'total_volume': fields.Integer,
    'price_average': fields.Float,
    'price_minimum': fields.Float,
    'price_maximum': fields.Float,
    'order_count': fields.Integer,
}

order_list = {
    'orders': fields.List(fields.Nested(order)),
    'stats': fields.Nested(order_stats),
}


def fetch_item_market_stats(item_id):
    stats = MarketOrder \
        .query \
        .filter(MarketOrder.expire_time > datetime.utcnow()) \
        .filter_by(item_id=item_id) \
        .with_entities(
            func.sum(MarketOrder.amount).label('total_volume'),
            func.avg(MarketOrder.price).label('price_average'),
            func.min(MarketOrder.price).label('price_minimum'),
            func.max(MarketOrder.price).label('price_maximum'),
            func.count(MarketOrder.id).label('order_count'),
        ).one()

    return {
        'total_volume': stats.total_volume,
        'price_average': stats.price_average,
        'price_minimum': stats.price_minimum,
        'price_maximum': stats.price_maximum,
        'order_count': stats.order_count,
    }


class OrdersV1(Resource):
    @marshal_with(order_list)
    def get(self, item_id):
        orders = MarketOrder\
            .query\
            .filter(MarketOrder.expire_time > datetime.utcnow())\
            .filter_by(item_id=item_id)\
            .order_by(MarketOrder.price)

        return {
            'orders': orders,
            'stats': fetch_item_market_stats(item_id)
        }, 200
