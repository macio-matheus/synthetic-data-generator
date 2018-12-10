import os

import psycopg2

print("Connection postgres started: ")
conn_prod = psycopg2.connect(host='postgres', database='boticario',
                             user=os.environ['POSTGRES_USER'], password=os.environ['POSTGRES_PASSWORD'])

print("Connection postgres-admin started: ")
conn_admin = psycopg2.connect(host='postgres-admin', database='boticario_admin',
                              user=os.environ['POSTGRES_USER'], password=os.environ['POSTGRES_PASSWORD'])


def query_prod(query):
    """
    recovery data from database by a select query
    :param query:
    :return: a list of tuples
    """
    object_cursor = conn_prod.cursor()
    object_cursor.execute(query)
    result = object_cursor.fetchall()
    conn_prod.commit()
    object_cursor.close()

    print(f'Query finish: [{query}]')

    return result


def query_admin(query):
    """
    recovery data from database by a select query
    :param query:
    :return: a list of tuples
    """
    object_cursor = conn_admin.cursor()
    object_cursor.execute(query)
    result = object_cursor.fetchall()
    conn_admin.commit()
    object_cursor.close()

    print(f'Query finish: [{query}]')

    return result
