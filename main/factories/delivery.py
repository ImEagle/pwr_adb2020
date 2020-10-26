from datetime import datetime
from uuid import uuid4

import factory.fuzzy
import pytz

import config
from factories._choices import DELIVERY_CHOICES
from factories.employee import EmployeeFactory
from factories.order import OrderFactory
from models.delivery import Delivery


class DeliveryFactory(factory.Factory):
    delivery_id = factory.LazyAttribute(lambda o: str(uuid4()))
    order_id = factory.SubFactory(OrderFactory)
    employee_id = factory.SubFactory(EmployeeFactory)
    pick_up_at = factory.fuzzy.FuzzyDateTime(datetime.now(pytz.UTC))
    delivered_at = factory.fuzzy.FuzzyDateTime(datetime.now(pytz.UTC))
    type = factory.fuzzy.FuzzyChoice(DELIVERY_CHOICES)
    tip = factory.fuzzy.FuzzyFloat(
        config.DELIVERY_TIP_FROM,
        config.DELIVERY_TIP_TO,
        precision=2
    )

    class Meta:
        model = Delivery
