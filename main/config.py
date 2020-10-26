from datetime import datetime

import pytz

db_host = "db"
db_name = "adb_project"
db_user = "adb_project"
db_pass = "password"

# === LOCATIONS ===
LOCATIONS_AMOUNT = 10

LOCATION_CREATED_AT_FROM = datetime(2010, 1, 1, tzinfo=pytz.UTC)
LOCATION_CREATED_AT_TO = datetime.now(pytz.UTC)

# === CUSTOMER ===
CUSTOMERS_AMOUNT = 100

CUSTOMER_DATE_OF_BIRTH_FROM = datetime(1990, 1, 1, tzinfo=pytz.UTC)
CUSTOMER_DATE_OF_BIRTH_TO = datetime(2010, 1, 1, tzinfo=pytz.UTC)
CUSTOMER_CREATED_AT_FROM = datetime(2010, 1, 1, tzinfo=pytz.UTC)
CUSTOMER_CREATED_AT_TO = datetime.now(pytz.UTC)
CUSTOMER_UPDATED_AT_FROM = datetime(2010, 1, 1, tzinfo=pytz.UTC)
CUSTOMER_UPDATED_AT_TO = datetime.now(pytz.UTC)

# === CUSTOMER LOCATIONS ===
# Number of locations assigned to the Customer
CUSTOMER_LOCATIONS = (1, 2)

CUSTOMER_LOCATION_CREATED_AT_FROM = datetime(2010, 1, 1, tzinfo=pytz.UTC)
CUSTOMER_LOCATION_CREATED_AT_TO = datetime.now(pytz.UTC)

# === Employees ===
EMPLOYEES_AMOUNT = 50

EMPLOYEE_EMPLOYMENT_DATE_FROM = datetime(2010, 1, 1, tzinfo=pytz.UTC)
EMPLOYEE_EMPLOYMENT_DATE_TO = datetime.now(pytz.UTC)

# === DELIVERY ===
DELIVERY_PICK_UP_AT_MINUTES_FROM = 5
DELIVERY_PICK_UP_AT_MINUTES_TO = 100

DELIVERY_DELIVERY_AT_MINUTES_FROM = 20
DELIVERY_DELIVERY_AT_MINUTES_TO = 120

DELIVERY_TIP_FROM = 0.
DELIVERY_TIP_TO = 10.

# === Item ===
# Number of items sold by the Vendor
VENDOR_ITEMS = (1, 50)

ITEM_CREATED_AT_MINUTES_FROM = 1
ITEM_CREATED_AT_MINUTES_TO = 3000

ITEM_PRICE_FROM = 1.
ITEM_PRICE_TO = 20.

# === VENDOR ===
VENDOR_CATEGORIES_AMOUNT = 50

VENDORS_AMOUNT = 100

ORDERS_ITEMS_AMOUNT = (1, 20)

# === ORDERS ===
# Orders created per Customer
ORDERS_AMOUNT = (1000, 100000)

ORDER_CREATED_AT_FROM = datetime(2010, 1, 1, tzinfo=pytz.UTC)
ORDER_CREATED_AT_TO = datetime.now(pytz.UTC)

ORDER_PREPARED_AT_MINUTES_FROM = 10
ORDER_PREPARED_AT_MINUTES_TO = 60

# === PROMOTIONS ===
# Promotions created per Customer
PROMOTIONS_AMOUNT = (0, 100)

PROMOTION_START_DATE_DAYS_FROM = 10
PROMOTION_START_DATE_DAYS_TO = 10000
