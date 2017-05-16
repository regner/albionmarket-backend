

from datetime import datetime, timedelta
from flask_restful import Resource

from ..models import MarketOrder


class StatsV1(Resource):
    def get(self):
        added_last_hour = MarketOrder.query.filter(MarketOrder.ingest_time >= datetime.utcnow() - timedelta(hours=1)).count()
        added_last_day = MarketOrder.query.filter(MarketOrder.ingest_time >= datetime.utcnow() - timedelta(days=1)).count()
        active_orders = MarketOrder.query.filter(MarketOrder.expire_time >= datetime.utcnow()).count()

        return {
            'added_last_hour': added_last_hour,
            'added_last_day': added_last_day,
            'active_orders': active_orders,
        }, 200
