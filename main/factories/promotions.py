from datetime import datetime

import factory.fuzzy

from factories._choices import PROMOTION_TYPE
from factories.items import ItemFactory
from factories.vendors import VendorFactory
from models.promotions import Promotion, PromotionItem


class PromotionItemFactory(factory.Factory):
    promotion_id = factory.fuzzy.FuzzyInteger(1, 100000000)
    item_id = factory.SubFactory(ItemFactory)
    type = factory.fuzzy.FuzzyChoice(PROMOTION_TYPE)
    min_items_count = factory.fuzzy.FuzzyInteger(1, 5)
    max_items_count = factory.fuzzy.FuzzyInteger(10, 20)
    discount_amount = factory.fuzzy.FuzzyFloat(0., 5.)
    discount_percent = factory.fuzzy.FuzzyFloat(0., 50.)

    class Meta:
        model = PromotionItem


class PromotionFactory(factory.Factory):
    promotion_id = factory.fuzzy.FuzzyInteger(1, 100000000)
    vendor_id = factory.SubFactory(VendorFactory)
    name = factory.fuzzy.FuzzyText()
    start_date = factory.fuzzy.FuzzyDateTime(datetime.now())
    end_date = factory.fuzzy.FuzzyDateTime(datetime.now())
    type = factory.fuzzy.FuzzyChoice(PROMOTION_TYPE)
    discount_amount = factory.fuzzy.FuzzyFloat(0., 5.)
    discount_percent = factory.fuzzy.FuzzyFloat(0., 50.)

    class Meta:
        model = Promotion
