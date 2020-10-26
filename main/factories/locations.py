from datetime import datetime

import factory.fuzzy
import pytz

from models.locations import Location


class LocationFactory(factory.Factory):
    location_id = factory.fuzzy.FuzzyInteger(1, 100000000)
    name = factory.fuzzy.FuzzyText()
    location_type = factory.fuzzy.FuzzyText()
    country = factory.fuzzy.FuzzyText()
    address = factory.fuzzy.FuzzyText()
    latitude = factory.fuzzy.FuzzyFloat(0.1)
    longitude = factory.fuzzy.FuzzyFloat(0.1)
    created_at = factory.fuzzy.FuzzyDateTime(datetime.now(pytz.UTC))

    class Meta:
        model = Location
