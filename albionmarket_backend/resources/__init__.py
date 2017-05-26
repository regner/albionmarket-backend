

from .ingest import IngsetV1
from .orders import OrdersV1
from .orders_stats import OrdersStatsV1
from .orders_resources import OrdersResourcesV1
from .items import ItemsV1
from .categories import CategoriesV1
from .stats import StatsV1


def configure_resources(api):
    api.add_resource(IngsetV1, '/api/v1/ingest/')
    api.add_resource(OrdersV1, '/api/v1/orders/<string:item_id>/')
    api.add_resource(OrdersStatsV1, '/api/v1/orders/<string:item_id>/stats/')
    api.add_resource(OrdersResourcesV1, '/api/v1/orders/resources/')
    api.add_resource(ItemsV1, '/api/v1/items/')
    api.add_resource(CategoriesV1, '/api/v1/categories/')
    api.add_resource(StatsV1, '/api/v1/stats/')
