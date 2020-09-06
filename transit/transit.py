import json
import os

from db import DB
from pravah import Pravah
from google.protobuf.json_format import MessageToJson

channel = '/PublicBus'

geospace = [
    '/in/haryana/gurugram',
    '/in/delhi',
    '/in/mp/indore',
    '/in/maharastra/pune',
    '/in/karnataka/mysore',
    '/us/oregon/portland',
    '/us/kentucky/louisville',
    '/us/massachusetts/bostonMetro',
    '/us/california/contraCostaCounty',
    '/us/connecticut',
    '/us/mta',
    '/aus/nsw',
    '/aus/victoria/kingston'
]

def start():
    c = Pravah(
        channel,
        endpoint='rpc.pravah.io:6666',
        auth_token=os.getenv('PRAVAH_API_KEY')
    )
    feed = c.subscribe(geospace)

    db = DB(channel)

    for m, c in feed:
        jsonObj = json.loads(MessageToJson(m))
        obj = db.insert(c, jsonObj)
        #print(jsonObj)
        print(channel + ': ' + str(obj) + ' [' + c + ']')

if '__main__' == __name__:
    start()