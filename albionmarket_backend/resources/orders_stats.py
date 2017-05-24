

from flask_restful import Resource, marshal_with

from .orders import fetch_item_market_stats, order_stats


class OrdersStatsV1(Resource):
    @marshal_with(order_stats)
    def get(self, item_id):
        return fetch_item_market_stats(item_id), 200
