

import json

from flask_script import Command

from .. import models


class SeedData(Command):
    def run(self):
        with open('seeddata/categories.json') as categories_file:
            categories = json.load(categories_file)

            for category in categories:
                models.Category.create_or_update(category['id'], category['name'])

        with open('seeddata/sub_categories.json') as sub_categories_file:
            sub_categories = json.load(sub_categories_file)

            for category in sub_categories:
                models.SubCategory.create_or_update(category['id'], category['name'])

        with open('seeddata/items.json') as items_file:
            items = json.load(items_file)

            for item in items:
                models.Item.create_or_update(item['id'], item['name'], item['tier'], item['category'], item['sub_category'])
