import json
import time

import os
import random

time.sleep(15)

import numpy as np

from connectors_db.postgres_db import query_prod, query_admin
from connectors_db.mongo_db import Mongo
from data_generator.generator import (
    BASECOMPRASPDV_DDL,
    SELLOUT_TB_LOJA_VENDA_SO_DDL,
    BASECONSUMIDOR_BOT_DDL,
    BASECOMPRASECM_DDL,
    gera_sql,
    corrompe_campo
)
from data_publisher.kafka_lib import KafkaClient

QUANTITY_RECORDS_PER_TABLE = int(os.environ['QUANTIY_RECORDS'])
QUANTITY_RECORDS_WITH_NOISE_PER_TABLE = int(
    (QUANTITY_RECORDS_PER_TABLE * int(os.environ['QUANTIY_RECORDS_NOISE_PERCENT'])) / 100)

noise_threshold = 0.3


def populate_postgre():
    """
    Populate postgree db
    :return:
    """

    print("-- POSTGRES INIT --")

    tables_name = ['BASECOMPRASPDV_DDL', 'SELLOUT_TB_LOJA_VENDA_SO_DDL', 'BASECONSUMIDOR_BOT_DDL',
                   'BASECOMPRASECM_DDL']
    tables = [BASECOMPRASPDV_DDL, SELLOUT_TB_LOJA_VENDA_SO_DDL, BASECONSUMIDOR_BOT_DDL, BASECOMPRASECM_DDL]
    noise = False

    for index, t in enumerate(tables):
        for i in range(QUANTITY_RECORDS_PER_TABLE):
            if random.random() < noise_threshold:
                t().info, _ = corrompe_campo(t().info)
                noise = True
            cmd_insert = gera_sql(t().info, tables_name[index])
            id_reg = query_prod(cmd_insert)[0][0]

            if noise:
                sql = f'insert into register_noise (id_input_with_noise, provider) values ({id_reg}, \'{os.environ["PROVIDER"]}\') returning ID'
                query_admin(sql)
                noise = False
    print("-- POSTGRES INSERTS END --")


def populate_postgre_streaming():
    """
    Populate postgree db streaming
    :return:
    """
    noise = False
    t = BASECOMPRASECM_DDL()
    if random.random() < noise_threshold:
        t.info, _ = corrompe_campo(t.info)
        noise = True
    cmd_insert = gera_sql(t.info, 'BASECOMPRASECM_DDL')
    id_reg = query_prod(cmd_insert)[0][0]

    if noise:
        sql = f'insert into register_noise (id_input_with_noise, provider) values ({id_reg}, \'{os.environ["PROVIDER"]}\') returning ID'
        query_admin(sql)


def populate_mongodb():
    """
    Generate data for mongodb
    :return:
    """
    print("-- MONGODB INIT --")

    collections_name = ["BASECOMPRASPDV_DDL", "BASECONSUMIDOR_BOT_DDL", "SELLOUT_TB_LOJA_VENDA_SO_DDL",
                        "BASECOMPRASECM_DDL"]

    database_name = os.environ['MONGO_DB_NAME']
    mongo_client = Mongo(database_name)

    for collection_name in collections_name:
        for num_record in range(QUANTITY_RECORDS_PER_TABLE):
            object_table = globals()[collection_name]()
            data = object_table.info
            if random.random() < noise_threshold:
                data, _ = corrompe_campo(data)

            mongo_client.insert_document(data, collection_name)
    print("-- MONGODB INSERTS END --")


def run_data_streaming(delay=3):
    print("-- INIT KAFKA --")
    kafka_client = KafkaClient()

    topicts_name = ["BASECOMPRASPDV_DDL",
                    "BASECONSUMIDOR_BOT_DDL",
                    "SELLOUT_TB_LOJA_VENDA_SO_DDL"]

    while True:
        for topic_name in topicts_name:
            sintetic_data = globals()[topic_name]().info
            sintetic_data = json.dumps(sintetic_data, default=str)

            print("Publishing to topic ", topic_name)
            print(sintetic_data, "\n")
            kafka_client.send_json(topic_name, sintetic_data)

        populate_postgre_streaming()
        print("-- POSTGRES RUNNING STREAMING... --")

        time.sleep(delay)
        print("-- KAFKA RUNNING... --")


def run():
    kafka_client = KafkaClient()
    envs = dict(os.environ)
    print(envs)
    kafka_client.send_json("logs", envs)

    populate_postgre()
    populate_mongodb()
    run_data_streaming()


if __name__ == '__main__':
    run()
