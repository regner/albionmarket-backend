

from ..extensions import db


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)

    items = db.relationship('Item', backref='category', lazy='dynamic')

    def __init__(self, category_id, name):
        self.id = category_id
        self.name = name

    @classmethod
    def create_or_update(cls, category_id, name):
        category = Category.query.get(category_id)

        if category is None:
            category = cls(category_id, name)

        category.name = name

        db.session.add(category)
        db.session.commit()
