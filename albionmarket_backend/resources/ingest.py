

import json
import dateutil.parser

from flask_restful import Resource, reqparse, abort

from ..models import MarketOrder


class IngsetV1(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('MarketItems', type=list, location='json', required=True)
        parser.add_argument('LocationId', type=int, location='json', required=True)
        args = parser.parse_args()

        if not all(isinstance(x, str) for x in args['MarketItems']):
            abort(400, description='Not all marketItems are strings.')

        for order in args['MarketItems']:
            order_json = json.loads(order)

            try:
                MarketOrder.create_or_update(
                    order_id=order_json['Id'],
                    item_id=order_json['ItemTypeId'],
                    location_id=args['LocationId'],
                    quality=order_json['QualityLevel'],
                    enchantment=order_json['EnchantmentLevel'],
                    price=order_json['UnitPriceSilver'],
                    amount=order_json['Amount'],
                    expire=dateutil.parser.parse(order_json['Expires']),
                )

            except KeyError:
                abort(400, description='JSON market order did not have all required fields.')

        return {}, 201
