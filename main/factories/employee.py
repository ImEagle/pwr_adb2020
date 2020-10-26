from datetime import datetime

import factory.fuzzy

from factories._choices import GENDER_CHOICES, EMPLOYEE_TYPE
from models.employee import Employee


class EmployeeFactory(factory.Factory):
    employee_id = factory.fuzzy.FuzzyInteger(1, 100000000)
    first_name = factory.fuzzy.FuzzyText()
    last_name = factory.fuzzy.FuzzyText()
    access_code = factory.fuzzy.FuzzyInteger(1000, 9999)
    gender = factory.fuzzy.FuzzyChoice(GENDER_CHOICES)
    employment_date = factory.fuzzy.FuzzyDate(datetime.now().date())
    type = factory.fuzzy.FuzzyChoice(EMPLOYEE_TYPE)

    class Meta:
        model = Employee
