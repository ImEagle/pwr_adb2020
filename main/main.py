import random
from dataclasses import asdict
from datetime import timedelta
from typing import List

import psycopg2

import config
from factories.customers import CustomerFactory, CustomerLocationFactory
from factories.delivery import DeliveryFactory
from factories.employee import EmployeeFactory
from factories.items import ItemFactory
from factories.locations import LocationFactory
from factories.order import OrderFactory, OrderItemFactory
from factories.promotions import PromotionFactory, PromotionItemFactory
from factories.ratings import RatingFactory
from factories.vendors import VendorCategoryFactory, VendorFactory
from models.customers import Customer
from models.employee import Employee
from models.items import Item
from models.locations import Location
from models.order import Order
from models.vendors import VendorCategory, Vendor


def _insert(cur, table_name, columns: List[str], items):
    insert_fields = ', '.join(columns)

    fields_arr = [f"%({c_name})s" for c_name in columns]
    fields_query_str = ', '.join(fields_arr)

    query = f"INSERT INTO {table_name}({insert_fields}) VALUES ({fields_query_str})"
    cur.executemany(
        query, items
    )


def migrate():
    conn = get_connection()
    cur = conn.cursor()

    file_name = "migrations/001_schema.sql"

    content = None

    with open(file_name) as f:
        content = f.read()

    cur.execute(content)
    conn.commit()


def create_locations():
    locations = []

    conn = get_connection()
    cur = conn.cursor()

    for _ in range(1, config.LOCATIONS_AMOUNT):
        location = LocationFactory()

        locations.append(asdict(location))

    _insert(cur, "locations", locations[0].keys(), locations)
    conn.commit()

    return locations


def create_customers_with_location(locations: List[Location]):
    locations_ids = [l["location_id"] for l in locations]
    min_locations, max_locations = config.CUSTOMER_LOCATIONS

    customers = []
    customers_locations = []

    for _ in range(1, config.CUSTOMERS_AMOUNT):
        customer = CustomerFactory()
        customers.append(asdict(customer))

        for _ in range(0, random.randrange(min_locations, max_locations)):
            cl = CustomerLocationFactory(
                customer_id=customer.customer_id,
                location_id=random.choice(locations_ids)
            )

            customers_locations.append(asdict(cl))

    conn = get_connection()
    cur = conn.cursor()

    _insert(cur, "customers", customers[0].keys(), customers)
    _insert(cur, "customers_location", customers_locations[0].keys(), customers_locations)
    conn.commit()

    return customers


def create_employees():
    employees = []

    for _ in range(1, config.EMPLOYEES_AMOUNT):
        employee = EmployeeFactory()

        employees.append(asdict(employee))

    conn = get_connection()
    cur = conn.cursor()
    _insert(cur, "employees", employees[0].keys(), employees)
    conn.commit()

    return employees


def create_vendors_categories():
    vendor_categories = []

    for _ in range(1, config.VENDOR_CATEGORIES_AMOUNT):
        vendor_category = VendorCategoryFactory()

        vendor_categories.append(asdict(vendor_category))

    conn = get_connection()
    cur = conn.cursor()
    _insert(cur, "vendors_categories", vendor_categories[0].keys(), vendor_categories)
    conn.commit()

    return vendor_categories


def create_vendors(vendors_categories: List[VendorCategory], locations: List[Location]):
    vendors = []

    for _ in range(1, config.VENDORS_AMOUNT):
        vendor = VendorFactory(
            vendor_category_id=random.choice(vendors_categories)["vendor_category_id"],
            location_id=random.choice(locations)["location_id"],
        )

        vendors.append(asdict(vendor))

    conn = get_connection()
    cur = conn.cursor()
    _insert(cur, "vendors", vendors[0].keys(), vendors)
    conn.commit()

    return vendors


def create_items(vendors: List[Vendor]):
    min_items, max_items = config.VENDOR_ITEMS

    items = []

    for vendor in vendors:
        for _ in range(1, random.randrange(min_items, max_items)):
            created_at_delta = timedelta(minutes=random.randrange(
                config.ITEM_CREATED_AT_MINUTES_FROM,
                config.ITEM_CREATED_AT_MINUTES_TO
            ))

            item = ItemFactory(
                vendor_id=vendor["vendor_id"],
                created_at=vendor["created_at"] + created_at_delta
            )
            items.append(asdict(item))

    conn = get_connection()
    cur = conn.cursor()

    _insert(cur, "items", items[0].keys(), items)
    conn.commit()

    return items


def get_connection():
    conn = psycopg2.connect(
        host=config.db_host,
        database=config.db_name,
        user=config.db_user,
        password=config.db_pass
    )

    return conn


def create_orders(customers: List[Customer], employees: List[Employee], vendors: List[Vendor]):
    orders = []

    orders_min, orders_max = config.ORDERS_AMOUNT

    for customer in customers:
        for _ in range(1, random.randrange(orders_min, orders_max)):
            order = OrderFactory(
                customer_id=customer["customer_id"],
                employee_id=random.choice(employees)["employee_id"],
                vendor_id=random.choice(vendors)["vendor_id"],
                promotion_id=None
            )
            prepared_at_delta = timedelta(minutes=random.randrange(
                config.ORDER_PREPARED_AT_MINUTES_FROM, config.ORDER_PREPARED_AT_MINUTES_TO
            ))
            order.prepared_at = order.created_at + prepared_at_delta

            orders.append(asdict(order))

    conn = get_connection()
    cur = conn.cursor()
    _insert(cur, "orders", orders[0].keys(), orders)
    conn.commit()

    return orders


def create_orders_items(orders: List[Order], items: List[Item]):
    orders_items = []
    min_order_items, max_order_items = config.ORDERS_ITEMS_AMOUNT

    for order in orders:
        items_count_order = random.randrange(min_order_items, max_order_items)

        for item in items[:items_count_order]:
            order_item = OrderItemFactory(
                order_id=order["order_id"],
                item_id=item["item_id"]
            )

            orders_items.append(asdict(order_item))

    conn = get_connection()
    cur = conn.cursor()
    _insert(cur, "orders_has_items", orders_items[0].keys(), orders_items)
    conn.commit()

    return orders_items


def create_delivery(orders: List[Order], employees: List[Employee]):
    deliveries = []

    for order in orders:
        pick_up_at_delta = timedelta(
            minutes=random.randrange(
                config.DELIVERY_PICK_UP_AT_MINUTES_FROM,
                config.DELIVERY_TIP_TO
            )
        )
        delivered_at_delta = timedelta(
            minutes=random.randrange(
                config.DELIVERY_PICK_UP_AT_MINUTES_FROM,
                config.DELIVERY_PICK_UP_AT_MINUTES_TO
            )
        )

        delivery = DeliveryFactory(
            order_id=order["order_id"],
            employee_id=random.choice(employees)["employee_id"],
            pick_up_at=order['prepared_at'] + pick_up_at_delta,
            delivered_at=order['prepared_at'] + delivered_at_delta,
        )

        deliveries.append(asdict(delivery))

    conn = get_connection()
    cur = conn.cursor()
    _insert(cur, "delivery", deliveries[0].keys(), deliveries)
    conn.commit()

    return deliveries


def create_ratings(orders: List[Order]):
    ratings = []

    for order in orders:
        rating = RatingFactory(
            order_id=order["order_id"]
        )

        ratings.append(asdict(rating))

    conn = get_connection()
    cur = conn.cursor()
    _insert(cur, "ratings", ratings[0].keys(), ratings)
    conn.commit()

    return ratings


def create_promotions(vendors: List[Vendor]):
    promotions = []

    promotions_min, promotions_max = config.PROMOTIONS_AMOUNT

    for vendor in vendors:
        for _ in range(1, random.randrange(promotions_min, promotions_max)):
            start_date_delta = timedelta(days=config.PROMOTION_START_DATE_DAYS_FROM)
            end_date_delta = timedelta(days=config.PROMOTION_START_DATE_DAYS_TO)

            promotion = PromotionFactory(
                vendor_id=vendor["vendor_id"],
                start_date=vendor["created_at"] + start_date_delta,
                end_date=vendor["created_at"] + end_date_delta
            )

            promotions.append(asdict(promotion))

    conn = get_connection()
    cur = conn.cursor()
    _insert(cur, "promotions", promotions[0].keys(), promotions)
    conn.commit()

    return promotions


def create_promotions_items(promotions, items):
    promotions_items = []
    items_ids = [i["item_id"] for i in items]

    promotions_min, promotions_max = config.PROMOTIONS_ITEMS_AMOUNT

    for promotion in promotions:
        used_items = []

        for _ in range(1, random.randrange(promotions_min, promotions_max)):

            selected_item_id = random.choice(items_ids)
            while selected_item_id in used_items:
                selected_item_id = random.choice(items_ids)

            used_items.append(selected_item_id)

            promotion_item = PromotionItemFactory(
                promotion_id=promotion['promotion_id'],
                items_id=selected_item_id,
            )

            promotions_items.append(asdict(promotion_item))

    conn = get_connection()
    cur = conn.cursor()
    _insert(cur, "promotions_items", promotions_items[0].keys(), promotions_items)
    conn.commit()

    return promotions


def gen_all():
    employees = create_employees()
    locations = create_locations()
    customers = create_customers_with_location(locations)

    vendors_categories = create_vendors_categories()
    vendors = create_vendors(vendors_categories, locations)
    items = create_items(vendors)

    orders = create_orders(customers, employees, vendors)
    orders_items = create_orders_items(orders, items)

    deliveries = create_delivery(orders, employees)
    promotions = create_promotions(vendors)
    ratings = create_ratings(orders)

    promotion_items = create_promotions_items(promotions, items)

if __name__ == "__main__":

    gen_all()
