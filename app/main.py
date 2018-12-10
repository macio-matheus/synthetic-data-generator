import os
import random

import numpy as np

from connectors_db.postgres_db import query_prod, query_admin
from connectors_db.mongo_db import Mongo
from data_generator.generator import (
    BASECOMPRASPDV_DDL,
    SELLOUT_TB_LOJA_VENDA_SO_DDL,
    BASECONSUMIDOR_BOT_DDL,
    gera_sql,
    corrompe_campo
)
from data_publisher.publish_app import run_kafka_publisher

tables_name = ['BASECOMPRASPDV_DDL', 'SELLOUT_TB_LOJA_VENDA_SO_DDL', 'BASECONSUMIDOR_BOT_DDL', 'BASECOMPRASECM_DDL']

QUANTITY_RECORDS_PER_TABLE = int(os.environ['QUANTIY_RECORDS'])
QUANTITY_RECORDS_WITH_NOISE_PER_TABLE = int(
    (QUANTITY_RECORDS_PER_TABLE * int(os.environ['QUANTIY_RECORDS_NOISE_PERCENT'])) / 100)

np.random.seed(0)


def populate_postgre():
    """
    Populate postgree db
    :return:
    """

    print("-- POSTGRES INIT --")

    tables_name = ['BASECOMPRASPDV_DDL', 'SELLOUT_TB_LOJA_VENDA_SO_DDL', 'BASECONSUMIDOR_BOT_DDL',
                   'BASECOMPRASECM_DDL']
    tables = [BASECOMPRASPDV_DDL(), SELLOUT_TB_LOJA_VENDA_SO_DDL(), BASECONSUMIDOR_BOT_DDL()]

    for index, t in enumerate(tables):
        for i in range(QUANTITY_RECORDS_PER_TABLE):
            for k in range(QUANTITY_RECORDS_WITH_NOISE_PER_TABLE):
                t.info, _ = corrompe_campo(t.info)
                noise = True
            cmd_insert = gera_sql(t.info, tables_name[index])
            id_reg = query_prod(cmd_insert)[0][0]

            if noise:
                sql = f'insert into register_noise (id_input_with_noise, provider) values ({id_reg}, \'{os.environ["PROVIDER"]}\') returning ID'
                query_admin(sql)
                noise = False
    print("-- POSTGRES INSERTS END --")


def populate_mongodb():
    """
    Generate data for mongodb
    :return:
    """
    print("-- MONGODB INIT --")
    noise_threshold = 0.3
    collections_name = ["BASECOMPRASPDV_DDL", "BASECONSUMIDOR_BOT_DDL", "SELLOUT_TB_LOJA_VENDA_SO_DDL"]

    database_name = 'boticario'
    mongo_client = Mongo(database_name)

    for collection_name in collections_name:
        for num_record in range(QUANTITY_RECORDS_PER_TABLE):
            object_table = globals()[collection_name]()
            data = object_table.info
            if random.random() < noise_threshold:
                data, _ = corrompe_campo(data)

            mongo_client.insert_document(data, collection_name)
    print("-- MONGODB INSERTS END --")


if __name__ == '__main__':
    populate_postgre()
    populate_mongodb()
    run_kafka_publisher()
