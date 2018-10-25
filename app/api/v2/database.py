"""Module creates a connection to the database

Creates tables for the application
"""

import sys

import psycopg2
from instance.config import config

def init_db(db_url=None):
    """Initialize db connection
        
    Run queries that set up tables
    """
    try:
        conn, cursor = query_database()
        queries = drop_table_if_exists() + create_tables()
        i = 0
        while i != len(queries):
            query = queries[i]
            cursor.execute(query)
            conn.commit()
            i += 1
        conn.close()

    except Exception as error:
        print("\nQuery not executed : {} \n".format(error))


def create_tables():
    """Queries for setting up the database tables"""

    users_table_query = """
    CREATE TABLE users (
        user_id SERIAL PRIMARY KEY,
        email VARCHAR (30) NOT NULL UNIQUE,
        password VARCHAR (128) NOT NULL,
        role VARCHAR (10) NOT NULL
    )"""

    products_table_query = """
    CREATE TABLE products (
        product_id SERIAL PRIMARY KEY,
        product_name VARCHAR (24) NOT NULL,
        product_price INTEGER NOT NULL,
        category VARCHAR (50) NOT NULL
    )"""

    sales_order_query = """
    CREATE TABLE saleorders (
        sale_order_id SERIAL PRIMARY KEY,
        date_ordered TIMESTAMP DEFAULT NOW(),
        product_name VARCHAR (24) NOT NULL,
        product_price INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        amount INTEGER NOT NULL
    )"""

    return [users_table_query, products_table_query, sales_order_query]


def drop_table_if_exists():
    """Drop tables before recreating them"""

    drop_products_table = """
    DROP TABLE IF EXISTS products"""

    drop_sales_table = """
    DROP TABLE IF EXISTS saleorders"""

    drop_users_table = """
    DROP TABLE IF EXISTS users"""

    return [drop_products_table, drop_sales_table, drop_users_table]


def query_database(query=None, db_url=None):
    """Creates a connection to the db
        
    Executes a query
    """
    conn = None
    if db_url is None:
        db_url = config['db_url']
    try:
        # connect to db
        conn = psycopg2.connect(db_url)
        print("\n\nConnected {}\n".format(conn.get_dsn_parameters()))
        cursor = conn.cursor()

        if query:
            cursor.execute(query)
            conn.commit()

    except(Exception,
           psycopg2.DatabaseError,
           psycopg2.ProgrammingError) as error:
        print("DB ERROR: {}".format(error))

    return conn, cursor


def insert_to_db(query):
    """Handles INSERT queries"""
        
    try:
        conn = query_database(query)[0]
        conn.close()
    except psycopg2.Error as error:
        print("Insertion error: {}".format(error))
        sys.exit(1)


def select_from_db(query):
    """Handles SELECT queries"""
    
    fetched_content = None
    conn, cursor = query_database(query)
    if conn:
        fetched_content = cursor.fetchall()
        conn.close()

    return fetched_content


if __name__ == '__main__':
    init_db()
    query_database()
