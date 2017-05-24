

from flask_restful import Resource, marshal_with

from ..models import MarketOrder
from .orders import order_list


class OrdersRecentV1(Resource):
    @marshal_with(order_list)
    def get(self):
        orders = MarketOrder\
            .query\
            .order_by(MarketOrder.last_updated.desc())\
            .limit(100)

        return {
            'orders': orders,
        }, 200
