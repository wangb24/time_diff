'''
uses the stored date and time to calculate the difference between now and the stored date and time
'''

import os
import datetime
import json

def read_json():
    with open(f'{os.getcwd()}/data.json', 'r') as f:
        json_data = json.load(f)
    date = datetime.datetime(year=json_data['year'],
                             month=json_data['month'],
                             day=json_data['day'],
                             hour=json_data['hour'],
                             minute=json_data['minute'],
                             second=json_data['second']
                             )
    return date


def write_json(yr, m, d, h, mn, s):
    '''write date and time to data.json'''
    data = {
        'year': yr,
        'month': m,
        'day': d,
        'hour': h,
        'minute': mn,
        'second': s
    }
    with open(f'{os.getcwd()}/data.json', 'r') as f:
        with open(f'{os.getcwd()}/history', 'a') as f2:
            f2.write(f.read())
    with open(f'{os.getcwd()}/data.json', 'w') as f:
        json.dump(data, f)
