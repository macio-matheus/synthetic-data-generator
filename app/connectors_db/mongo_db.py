import os

from pymongo import MongoClient


class Mongo(object):

    def __init__(self, database_name):
        user_mongo = os.environ['MONGO_INITDB_ROOT_USERNAME']
        password_mongo = os.environ['MONGO_INITDB_ROOT_PASSWORD']
        cliente = MongoClient('db_mongo',
                              27017,
                              username=user_mongo,
                              password=password_mongo)

        self.database = cliente[database_name]

    def insert_document(self, document, collection_name):
        document_obj = self.database[collection_name]
        return document_obj.insert_one(document).inserted_id

    def get_document_by_id(self, document_id, collection_name):
        document_obj = self.database[collection_name]
        filter = {'id_': document_id}
        document_result = document_obj.find(filter)
        return list(document_result)

    def get_all(self, collection_name):
        docdocument_obj = self.database[collection_name]
        documents = docdocument_obj.find()
        return list(documents)
