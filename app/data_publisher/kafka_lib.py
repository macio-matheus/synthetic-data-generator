import os
import json

from kafka import KafkaConsumer
from kafka import KafkaProducer


class KafkaClient(object):

    def __init__(self):
        host = os.environ['KAFKA_ADVERTISED_HOST_NAME']
        port = 9092
        self._host = "{}:{}".format(host, port)
        print("Connecting kafka at ", self._host)

    def get_consumer(self, topic):
        print("getting a consumer for the topic", topic)
        consumer = KafkaConsumer(topic,
                                 bootstrap_servers=[self._host],
                                 enable_auto_commit=True,
                                 auto_offset_reset='latest',
                                 auto_commit_interval_ms=500)
        return consumer

    def send_message(self, topic, message):
        producer = KafkaProducer(bootstrap_servers=self._host,
                                 retries=5, api_version=(0, 10, 1))
        producer.send(topic, message.encode())
        producer.flush()
        producer.close()

    def send_json(self, topic, json_content):
        json_producer = KafkaProducer(bootstrap_servers=[self._host],
                                      value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                                      retries=5)
        json_producer.send(topic, json_content)

        json_producer.flush()


def test_sending_simple_messages():
    kafka_client = KafkaClient()

    text = """Como sabemos se funcionou? Além da resposta ao comando insert 
        (nInserted indica quantos documentos foram inseridos com o comando), 
        você pode executar o find novamente para ver que agora sim temos 
        customers no nosso banco de dados. Além disso, se executar o “show collections” 
        e o “show databases”, verá que agora sim possuímos uma coleção 
        customers e uma base workshop nesse servidor."""

    for line in text.split("\n"):
        kafka_client.send_message(topic="my_topic", message=line)


if __name__ == "__main__":
    test_sending_simple_messages()
