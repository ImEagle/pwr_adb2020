from uuid import uuid4

import factory.fuzzy

import config
from factories._choices import GENDER_CHOICES, EMPLOYEE_TYPE
from models.employee import Employee


class EmployeeFactory(factory.Factory):
    employee_id = factory.LazyAttribute(lambda o: str(uuid4()))
    first_name = factory.fuzzy.FuzzyText()
    last_name = factory.fuzzy.FuzzyText()
    access_code = factory.fuzzy.FuzzyInteger(1000, 9999)
    gender = factory.fuzzy.FuzzyChoice(GENDER_CHOICES)
    employment_date = factory.fuzzy.FuzzyDate(
        config.EMPLOYEE_EMPLOYMENT_DATE_FROM,
        config.EMPLOYEE_EMPLOYMENT_DATE_TO
    )
    type = factory.fuzzy.FuzzyChoice(EMPLOYEE_TYPE)

    class Meta:
        model = Employee
