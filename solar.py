import json
import os

from dlake import Datalake
from mesh_solar_power_production.main import MeshSolarPowerProduction
from google.protobuf.json_format import MessageToJson

geospace = [
    '/in/delhi'
]

def start():
    c = MeshSolarPowerProduction('rpc.pravah.io:5555')
    feed = c.subscribe(geospace)

    datalake = Datalake(os.getenv('PRAVAH_DB_USERNAME'), os.getenv('PRAVAH_DB_PASSWORD'), c.get_channel())

    for m, chan in feed:
        jsonObj = json.loads(MessageToJson(m))

        obj = datalake.insert(chan, jsonObj)
        print('[SOLAR] ' + str(obj) + ': ' + chan)

if '__main__' == __name__:
    start()