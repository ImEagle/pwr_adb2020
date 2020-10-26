from datetime import datetime

import factory.fuzzy

from factories.vendors import VendorFactory
from models.items import Item


class ItemFactory:
    item_id = factory.fuzzy.FuzzyInteger(1, 100000000)
    vendor_id = factory.SubFactory(VendorFactory)
    name = factory.fuzzy.FuzzyText
    price = factory.fuzzy.FuzzyFloat(1., 20.)
    created_at = factory.fuzzy.FuzzyDateTime(datetime.now())

    class Meta:
        model = Item
