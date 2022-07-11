import os
import json
import datetime
from funcs import file_op

def store_current_time():
    '''store current date and time in data.json'''
    now = datetime.datetime.utcnow()
    file_op.write_json(
        int(now.year),
        int(now.month),
        int(now.day),
        int(now.hour),
        int(now.minute),
        int(now.second)
    )


def get_difference():
    last_time = file_op.read_json()
    current_time = datetime.datetime.utcnow()
    difference = current_time - last_time
    seconds_in_day = 60 * 60 * 24
    m, s = divmod(difference.days * seconds_in_day + difference.seconds, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    return f'{d} days, {h} hours, {m} minutes, {s} seconds'