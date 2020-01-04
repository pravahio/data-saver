import json
import pytz

from dlake import Datalake
from datetime import datetime


def main():
    datalake = Datalake('pravah', '', '/SolarPowerProduction')
    station = 'kitpitampura'
    cur = datalake.get({
            'geospace': '/in/delhi',
            'item.stations.id': station
        }, past_hours=24)
    # start="2020/01/03 06:30:00", end="2020/01/03 23:30:00"


    for i in cur:
        for s in i['item']['stations']:
            if s['id'] != station:
                continue
            try:
                d = datetime.fromtimestamp(int(s['timestamp']))
            except:
                d = ''
            try:
                p = str(s['powerGenerationParameters']['currentPowerOutput'])
            except:
                p = ''
            print(str(i) + ' ' + str(s['id']) + ' \t: ' + str(d) + ' : ' + p)

if '__main__' == __name__:
    main()