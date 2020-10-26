from datetime import datetime

import factory.fuzzy
import pytz

from factories._choices import DELIVERY_CHOICES
from factories.employee import EmployeeFactory
from factories.order import OrderFactory
from models.delivery import Delivery


class DeliveryFactory(factory.Factory):
    delivery_id = factory.fuzzy.FuzzyInteger(1, 100000000)
    order_id = factory.SubFactory(OrderFactory)
    employee_id = factory.SubFactory(EmployeeFactory)
    pick_up_at = factory.fuzzy.FuzzyDateTime(datetime.now(pytz.UTC))
    delivered_at = factory.fuzzy.FuzzyDateTime(datetime.now(pytz.UTC))
    type = factory.fuzzy.FuzzyChoice(DELIVERY_CHOICES)
    tip = factory.fuzzy.FuzzyFloat(0., 10., precision=2)

    class Meta:
        model = Delivery
