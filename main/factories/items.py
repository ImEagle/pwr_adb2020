from datetime import datetime
from uuid import uuid4

import factory.fuzzy
import pytz

import config
from factories.vendors import VendorFactory
from models.items import Item


class ItemFactory(factory.Factory):
    item_id = factory.LazyAttribute(lambda o: str(uuid4()))
    vendor_id = factory.SubFactory(VendorFactory)
    name = factory.fuzzy.FuzzyText()
    price = factory.fuzzy.FuzzyFloat(
        config.ITEM_PRICE_FROM,
        config.ITEM_PRICE_TO
    )
    created_at = factory.fuzzy.FuzzyDateTime(datetime.now(pytz.UTC))

    class Meta:
        model = Item
