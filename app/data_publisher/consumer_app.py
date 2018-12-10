import json

from data_publisher.kafka_lib import KafkaClient


def consuming_simple_messages():
    kafka_client = KafkaClient()

    print("Consuming the messages")

    consumer = kafka_client.get_consumer(topic='my_topic')
    for message in consumer:
        # print("Message:", message.value.decode('utf-8'))
        print("Message:{}\n topic: {}\n Offset: {}\n".format(
            message.value.decode('utf-8'),
            message.topic,
            message.offset))

    consumer.close()


# consuming multiples topics on a json format
if __name__ == "__main__":

    collections_name = ["BASECOMPRASPDV_DDL",
                        "BASECONSUMIDOR_BOT_DDL",
                        "CA_CICLOS_DDL",
                        "SELLOUT_TB_LOJA_VENDA_SO_DDL"]

    kafka_client = KafkaClient()
    consumer = kafka_client.get_consumer(collections_name[0])
    consumer.subscribe(collections_name)

    for message in consumer:
        json_content = json.loads(message.value.decode('utf-8'))
        # print("Message:", message.value.decode('utf-8'))
        print("Message:{}\n topic: {}\n Offset: {}\n".format(
            json_content,
            message.topic,
            message.offset))

    consumer.close()
