from datetime import datetime
from uuid import uuid4

import factory.fuzzy
import pytz

import config
from factories._choices import ORDER_STATUS
from factories.customers import CustomerFactory
from factories.employee import EmployeeFactory
from factories.items import ItemFactory
from factories.promotions import PromotionFactory
from factories.vendors import VendorFactory
from models.order import OrderItem, Order


class OrderFactory(factory.Factory):
    order_id = factory.LazyAttribute(lambda o: str(uuid4()))
    customer_id = factory.SubFactory(CustomerFactory)
    employee_id = factory.SubFactory(EmployeeFactory)
    vendor_id = factory.SubFactory(VendorFactory)
    created_at = factory.fuzzy.FuzzyDateTime(
        config.ORDER_CREATED_AT_FROM,
        config.ORDER_CREATED_AT_TO
    )
    status = factory.fuzzy.FuzzyChoice(ORDER_STATUS)
    items_count = factory.fuzzy.FuzzyInteger(1)
    total_amount = factory.fuzzy.FuzzyFloat(1.)
    promotion_id = factory.SubFactory(PromotionFactory)
    prepared_at = factory.fuzzy.FuzzyDateTime(datetime.now(pytz.UTC))

    class Meta:
        model = Order


class OrderItemFactory(factory.Factory):
    order_id = factory.SubFactory(OrderFactory)
    item_id = factory.SubFactory(ItemFactory)
    quantity = factory.fuzzy.FuzzyInteger(1, 10)
    comment = factory.fuzzy.FuzzyText()

    class Meta:
        model = OrderItem
