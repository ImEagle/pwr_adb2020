from datetime import datetime

import factory.fuzzy
import pytz

from factories.order import OrderFactory
from models.ratings import Rating


class RatingFactory(factory.Factory):
    rating_id = factory.fuzzy.FuzzyInteger(1, 100000000)
    order_id = factory.SubFactory(OrderFactory)
    opinion = factory.fuzzy.FuzzyText()
    rating = factory.fuzzy.FuzzyInteger(0, 5)
    created_at = factory.fuzzy.FuzzyDateTime(datetime.now(pytz.UTC))

    class Meta:
        model = Rating
