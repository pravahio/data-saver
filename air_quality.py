import json
import os

from dlake import Datalake
from mesh_air_quality.main import MeshAirQuality
from google.protobuf.json_format import MessageToJson

geospace = [
    '/in/ncr'
]

def start():
    c = MeshAirQuality('rpc.pravah.io:5555')
    feed = c.subscribe(geospace)

    datalake = Datalake(os.getenv('PRAVAH_DB_USERNAME'), os.getenv('PRAVAH_DB_PASSWORD'), c.get_channel())

    for m, chan in feed:
        jsonObj = json.loads(MessageToJson(m, including_default_value_fields=True))

        obj = datalake.insert(chan, jsonObj)
        print('[AIR_QUALITY] ' + str(obj) + ': ' + chan)

if '__main__' == __name__:
    start()