from pymongo import MongoClient

import os


class ConnectionDb:

    @staticmethod
    def connect():
        try:
            client = MongoClient(os.getenv('DB_PORT_27017_TCP_ADDR'), 27017)
            db = client['test_doc']
            conn = db['logger_doc']
            return conn
        except ValueError as error:
            print(error)
