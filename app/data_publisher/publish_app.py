import json
import time

from data_publisher.kafka_lib import KafkaClient
from data_generator.generator import BASECOMPRASPDV_DDL, BASECONSUMIDOR_BOT_DDL, SELLOUT_TB_LOJA_VENDA_SO_DDL


collections_name = ["BASECOMPRASPDV_DDL",
                    "BASECONSUMIDOR_BOT_DDL",
                    "SELLOUT_TB_LOJA_VENDA_SO_DDL"]


def run_kafka_publisher(delay=1):
    print("-- INIT KAFKA --")
    kafka_client = KafkaClient()

    while True:
        for topic_name in collections_name:
            sintetic_data = globals()[topic_name]().info
            sintetic_data = json.dumps(sintetic_data, default=str)

            print("Publishing to topic ", topic_name)
            print(sintetic_data, "\n")
            kafka_client.send_json(topic_name, sintetic_data)

        time.sleep(delay)
        print("-- KAFKA RUNNING... --")
