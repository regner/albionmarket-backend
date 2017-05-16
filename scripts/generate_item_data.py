

import json


def pull_from_tuv(entry):
    if isinstance(entry['tuv'], list):
        for translation in entry['tuv']:
            if translation['{http://www.w3.org/XML/1998/namespace}lang'] == 'EN-US':
                return translation['seg']['$t']

    elif isinstance(entry['tuv'], dict):
        return entry['tuv']['seg']['$t']


def transform_localization_data(localization_data):
    item_data = {}
    market_categories = {}
    market_sub_categories = {}

    for entry in localization_data['tmx']['body']['tu']:
        try:
            prefix, name = entry['tuid'].split('_', 1)

        except ValueError:
            continue

        if name.endswith('_DESC'):
            continue

        if prefix == '@ITEMS':
            item_data[name] = pull_from_tuv(entry)

        elif prefix.startswith('@MARKETPLACEGUI'):
            if 'SHOPCATEGORY' in entry['tuid']:
                name = entry['tuid'].split('SHOPCATEGORY')[-1].strip('_').lower()
                value = pull_from_tuv(entry)

                market_categories[name] = value

            elif 'SHOPSUBCATEGORY' in entry['tuid']:
                name = entry['tuid'].split('SHOPSUBCATEGORY')[-1].strip('_').lower()
                value = pull_from_tuv(entry)

                market_sub_categories[name] = value

    return item_data, market_categories, market_sub_categories


def transform_item_data(item_data, localization_data):
    item_data = item_data['items']
    combined_items = item_data['farmableitem'] + \
                     item_data['stackableitem'] + \
                     item_data['consumableitem'] + \
                     item_data['equipmentitem'] + \
                     item_data['weapon'] + \
                     item_data['mount'] + \
                     item_data['furnitureitem'] + \
                     item_data['journalitem']

    data = []
    categories = set()
    sub_categories = set()

    for item in combined_items:
        data.append({
            'id': item['uniquename'],
            'name': localization_data[item['uniquename']] if item['uniquename'] in localization_data else 'NO TRANSLATION',
            'tier': item['tier'],
            'category': item['shopcategory'],
            'sub_category': item['shopsubcategory1'],
        })

        categories.add(item['shopcategory'])
        sub_categories.add(item['shopsubcategory1'])

    return data, list(categories), list(sub_categories)


def transform_category_data(categories, localization_data):
    return [{'id': x, 'name': localization_data[x]} for x in categories]


def main():
    with open('localization.json') as loc_file:
        item_loc, cat_loc, sub_cat_loc = transform_localization_data(json.load(loc_file))

    with open('items.json') as items_file:
        items, categories, sub_categories = transform_item_data(json.load(items_file), item_loc)

    with open('../seeddata/items.json', 'w') as out_file:
        json.dump(items, out_file)

    with open('../seeddata/categories.json', 'w') as out_file:
        json.dump(transform_category_data(categories, cat_loc), out_file)

    with open('../seeddata/sub_categories.json', 'w') as out_file:
        json.dump(transform_category_data(sub_categories, sub_cat_loc), out_file)


if __name__ == '__main__':
    main()