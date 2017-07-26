

from datetime import datetime

from ..extensions import db


class MarketOrder(db.Model):
    __tablename__ = 'market_orders'

    id = db.Column(db.Integer, primary_key=True)

    item_id = db.Column(db.String, db.ForeignKey('items.id'), nullable=False)
    location_id = db.Column(db.Integer, nullable=False)

    quality_level = db.Column(db.Integer, nullable=False)
    enchantment_level = db.Column(db.Integer, nullable=False)

    price = db.Column(db.BigInteger, nullable=False)
    amount = db.Column(db.Integer, nullable=False)

    is_buy_order = db.Column(db.Boolean, default=True)

    expire_time = db.Column(db.DateTime, nullable=False)
    ingest_time = db.Column(db.DateTime, nullable=False)
    last_updated = db.Column(db.DateTime, nullable=False)

    def __init__(self, order_id, item_id, location_id, quality, enchantment, price, amount, expire, is_buy_order):
        self.id = order_id

        self.item_id = item_id
        self.location_id = location_id

        self.quality_level = quality
        self.enchantment_level = enchantment

        self.price = price
        self.amount = amount

        self.is_buy_order = is_buy_order

        self.expire_time = expire
        self.ingest_time = datetime.utcnow()
        self.last_updated = datetime.utcnow()

    @classmethod
    def create_or_update(cls, order_id, item_id, location_id, quality, enchantment, price, amount, expire, is_buy_order):
        market_order = MarketOrder.query.get(order_id)

        if market_order is None:
            market_order = cls(order_id, item_id, location_id, quality, enchantment, price, amount, expire, is_buy_order)

        market_order.amount = amount
        market_order.last_updated = datetime.utcnow()

        db.session.add(market_order)
        db.session.commit()
