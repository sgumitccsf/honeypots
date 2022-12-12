#!/usr/bin/python3

import sys
from re import search
from ast import literal_eval
from datetime import datetime
from pymongo import MongoClient

try:
    client = MongoClient('mongodb://mongodb:mongodb@172.17.0.1:27017')
    print('Connection to MongoDB Success')
except:
    print('Connection to MongoDB Failed')

db = client['honeypot']
collection = db['honeypots']

for line in sys.stdin:
    filter1 = '"src_ip": "0.0.0.0"'
    filter2 = '"src_ip": "127.0.0.1"'
    filter3 = '"port_open.. 0.0.0.0 still open.."'
    if not search(filter1, line) and not search(filter2, line) and not search(filter3, line):
        try:
            data = literal_eval(line)
            data['timestamp'] = datetime.strptime(data['timestamp'], '%Y-%m-%dT%H:%M:%S.%f')
            collection.insert_one(data)
        except:
            sys.stdout.write(line)