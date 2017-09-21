# -*- coding: utf-8 -*-
from datetime import datetime as dt

import pandas as pd
from elasticsearch import Elasticsearch

df = pd.read_csv('nikkei_stock_average_daily_jp.csv', encoding='SHIFT-JIS')
es = Elasticsearch('http://localhost:9200')

def generate_doc(row):
    doc = {
        'start_value': row['start_value'],
        'end_value': row['end_value'],
        'low_value': row['low_value'],
        'high_value': row['high_value'],
        'timestamp': dt.strptime(row['date_day'], '%Y/%m/%d')
    }
    return doc

for row in df.iterrows():
    doc = generate_doc(row[1])
    type = 'nikkei225'
    res = es.index(index="stock", doc_type=type, id=str(row[0]), body=doc)
