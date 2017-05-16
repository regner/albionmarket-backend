

from ..extensions import db


class SubCategory(db.Model):
    __tablename__ = 'sub_categories'

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)

    items = db.relationship('Item', backref='sub_category', lazy='dynamic')

    def __init__(self, category_id, name):
        self.id = category_id
        self.name = name

    @classmethod
    def create_or_update(cls, category_id, name):
        category = SubCategory.query.get(category_id)

        if category is None:
            category = cls(category_id, name)

        category.name = name

        db.session.add(category)
        db.session.commit()
