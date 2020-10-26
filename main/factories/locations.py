from uuid import uuid4

import factory.fuzzy

import config
from models.locations import Location


class LocationFactory(factory.Factory):
    location_id = factory.LazyAttribute(lambda o: str(uuid4()))
    name = factory.fuzzy.FuzzyText()
    location_type = factory.fuzzy.FuzzyText()
    country = factory.fuzzy.FuzzyText()
    address = factory.fuzzy.FuzzyText()
    latitude = factory.fuzzy.FuzzyFloat(0.1)
    longitude = factory.fuzzy.FuzzyFloat(0.1)
    created_at = factory.fuzzy.FuzzyDateTime(
        config.LOCATION_CREATED_AT_FROM,
        config.LOCATION_CREATED_AT_TO
    )

    class Meta:
        model = Location
