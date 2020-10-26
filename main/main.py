import random
from dataclasses import asdict
from typing import List

import psycopg2

import config
from factories.customers import CustomerFactory, CustomerLocationFactory
from factories.locations import LocationFactory
from models.locations import Location


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


def get_connection():
    conn = psycopg2.connect(
        host=config.db_host,
        database=config.db_name,
        user=config.db_user,
        password=config.db_pass
    )

    return conn


if __name__ == "__main__":
    locations = create_locations()
    create_customers_with_location(locations)
