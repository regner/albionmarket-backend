

from datetime import datetime
from flask_restful import Resource, reqparse, fields, marshal_with

from .. import utils
from ..models import MarketOrder
from ..extensions import cache


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

order_list = {
    'orders': fields.List(fields.Nested(order)),
}


class OrdersV1(Resource):
    @cache.cached(key_prefix=utils.cache.make_cache_key)
    @marshal_with(order_list)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('location', type=int)
        parser.add_argument('type', type=str)
        args = parser.parse_args()

        filters = {}

        if args['location'] is not None:
            filters['location_id'] = args['location']

        if args['type'] is not None:
            filters['item_id'] = args['type']

        orders = MarketOrder\
            .query\
            .filter(MarketOrder.expire_time > datetime.utcnow()) \
            .filter_by(**filters)\
            .order_by(MarketOrder.amount)\
            .limit(50)

        return {
            'orders': orders,
        }, 200
