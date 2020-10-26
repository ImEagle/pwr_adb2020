from datetime import datetime

import factory.fuzzy
import pytz

from factories._choices import GENDER_CHOICES
from factories.locations import LocationFactory
from models.customers import Customer, CustomerLocation


class CustomerFactory(factory.Factory):
    customer_id = factory.fuzzy.FuzzyInteger(1, 100000000)
    gender = factory.fuzzy.FuzzyChoice(GENDER_CHOICES)
    date_of_birth = factory.fuzzy.FuzzyDate(datetime.now(pytz.UTC).date())
    is_active = True
    created_at = factory.fuzzy.FuzzyDateTime(datetime.now(pytz.UTC))
    updated_at = factory.fuzzy.FuzzyDateTime(datetime.now(pytz.UTC))
    first_name = factory.fuzzy.FuzzyText()
    last_name = factory.fuzzy.FuzzyText()

    class Meta:
        model = Customer


class CustomerLocationFactory(factory.Factory):
    customer_id = factory.SubFactory(CustomerFactory)
    location_id = factory.SubFactory(LocationFactory)
    created_at = factory.fuzzy.FuzzyDateTime(datetime.now(pytz.UTC))

    class Meta:
        model = CustomerLocation
