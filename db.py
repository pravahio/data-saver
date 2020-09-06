import os
from pymongo import MongoClient
import urllib.parse

class DB:
    def __init__(self, channel):
        username = os.getenv('PRAVAH_DB_USERNAME')
        password = os.getenv('PRAVAH_DB_PASSWORD')
        host = os.getenv('PRAVAH_DB_HOST')

        self.client = MongoClient(
            host,
            username=username,
            password=password,
            authSource='datalake',
            authMechanism='SCRAM-SHA-256'
        )
        self.db = self.client.datalake
        self.col = self.get_db_from_channel(channel)
    
    def get(self):
        col = self.db.publicbus
        print(col.find_one())
    
    def insert(self, geospace, obj):
        data = {
            'geospace': geospace,
            'item': obj
        }
        return self.db[self.col].insert(data)
    
    def get_db_from_channel(self, channel):
        return channel[1:].lower()

""" d = DB()
d.insert('/TestChannel', '/in/delhi', {
    'id': '234638463',
    'data': [
        {
            'first': 'ok',
            'second': 'not ok'
        }
    ]
}) """