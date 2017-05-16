

from ..extensions import db


class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    tier = db.Column(db.Integer, nullable=False)

    category_id = db.Column(db.String, db.ForeignKey('categories.id'), nullable=False)
    sub_category_id = db.Column(db.String, db.ForeignKey('sub_categories.id'), nullable=False)

    orders = db.relationship('MarketOrder', backref='item', lazy='dynamic')

    def __init__(self, item_id, name, tier, category, sub_category):
        self.id = item_id
        self.name = name
        self.tier = tier
        self.category_id = category
        self.sub_category_id = sub_category

    @classmethod
    def create_or_update(cls, item_id, name, tier, category, sub_category):
        item = Item.query.get(item_id)

        if item is None:
            item = cls(item_id, name, tier, category, sub_category)

        item.name = name

        db.session.add(item)
        db.session.commit()
