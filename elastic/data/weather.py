# -*- coding: utf-8 -*-
from datetime import datetime as dt

import pandas as pd
from elasticsearch import Elasticsearch

df = pd.read_csv('weather.csv', encoding='SHIFT-JIS')
es = Elasticsearch('http://localhost:9200')

def generate_doc(row):
    doc = {
        'low_value': row['low_temp'],
        'high_value': row['high_temp'],
        'timestamp': dt.strptime(row['timestamp'], '%Y/%m/%d')
    }
    return doc

for row in df.iterrows():
    doc = generate_doc(row[1])
    type = 'weatheryokohama'
    res = es.index(index="weather", doc_type=type, id=str(row[0]), body=doc)
