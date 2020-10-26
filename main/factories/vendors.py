from datetime import datetime

import factory.fuzzy
import pytz

from factories.locations import LocationFactory
from models.vendors import Vendor, VendorCategory


class VendorCategoryFactory(factory.Factory):
    vendor_category_id = factory.fuzzy.FuzzyInteger(1, 100000000)
    name = factory.fuzzy.FuzzyText()
    is_seasonal = False
    adults_only = False
    created_at = factory.fuzzy.FuzzyDateTime(datetime.now(pytz.UTC))

    class Meta:
        model = VendorCategory


class VendorFactory(factory.Factory):
    vendor_id = factory.fuzzy.FuzzyInteger(1, 100000000)
    vendor_category_id = factory.SubFactory(VendorCategoryFactory)
    location_id = factory.SubFactory(LocationFactory)
    name = factory.fuzzy.FuzzyText()
    delivery_charge = factory.fuzzy.FuzzyFloat(1., 5.)
    is_open = True
    created_at = factory.fuzzy.FuzzyDateTime(datetime.now(pytz.UTC))

    class Meta:
        model = Vendor
