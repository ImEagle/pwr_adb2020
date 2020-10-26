from uuid import uuid4

import factory.fuzzy

import config
from factories._choices import GENDER_CHOICES
from factories.locations import LocationFactory
from models.customers import Customer, CustomerLocation


class CustomerFactory(factory.Factory):
    customer_id = factory.LazyAttribute(lambda o: str(uuid4()))
    gender = factory.fuzzy.FuzzyChoice(GENDER_CHOICES)
    date_of_birth = factory.fuzzy.FuzzyDate(
        config.CUSTOMER_DATE_OF_BIRTH_FROM,
        config.CUSTOMER_DATE_OF_BIRTH_TO
    )
    is_active = factory.fuzzy.FuzzyChoice([True, False])
    created_at = factory.fuzzy.FuzzyDateTime(
        config.CUSTOMER_CREATED_AT_FROM,
        config.CUSTOMER_CREATED_AT_TO
    )
    updated_at = factory.fuzzy.FuzzyDateTime(
        config.CUSTOMER_UPDATED_AT_FROM,
        config.CUSTOMER_UPDATED_AT_TO
    )
    first_name = factory.fuzzy.FuzzyText()
    last_name = factory.fuzzy.FuzzyText()

    class Meta:
        model = Customer


class CustomerLocationFactory(factory.Factory):
    customer_id = factory.SubFactory(CustomerFactory)
    location_id = factory.SubFactory(LocationFactory)
    created_at = factory.fuzzy.FuzzyDateTime(
        config.CUSTOMER_LOCATION_CREATED_AT_FROM,
        config.CUSTOMER_LOCATION_CREATED_AT_TO
    )

    class Meta:
        model = CustomerLocation
