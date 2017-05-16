

from .ingest import IngsetV1
from .orders import OrdersV1
from .items import ItemsV1
from .categories import CategoriesV1
from .stats import StatsV1


def configure_resources(api):
    api.add_resource(IngsetV1, '/api/v1/ingest/')
    api.add_resource(OrdersV1, '/api/v1/orders/')
    api.add_resource(ItemsV1, '/api/v1/items/')
    api.add_resource(CategoriesV1, '/api/v1/categories/')
    api.add_resource(StatsV1, '/api/v1/stats/')
