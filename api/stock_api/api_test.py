"""
    Author: Ojelle Rogero
    Email: ojelle.rogero@gmail.com
    Created on: August 3, 2021
"""

#from fastquant import get_pse_data
#df1 = get_pse_data("2GO", "2016-01-04", "2016-01-08")
#print(df1.head())

import requests
import pandas as pd
import dateutil.parser

directory = r'C:\Users\ojell\Desktop\Oj\_Thesis\Data\stock_price'

base_url = r'https://pselookup.vrymel.com/api'
sym = '2GO'
per = ['2020-12-01', '2021-07-30']

response = requests.get(
    base_url + f'/stocks/{sym}/history/{per[0]}/{per[1]}',
    proxies={
        "http": "http://4f98f438b655416f86756d54b54f557f:@proxy.crawlera.com:8011/",
        "https": "https://4f98f438b655416f86756d54b54f557f:@proxy.crawlera.com:8011/",
    },
    verify='/path/to/zyte-smartproxy-ca.crt'
)

#response = requests.get(base_url + f'/stocks/{sym}/history/{per[0]}/{per[1]}')
data_json = response.json()
df = pd.DataFrame(data_json['history'])
#df['timestamp'] = df['timestamp'].apply(lambda x: dateutil.parser.isoparse(x).strftime('%Y-%m-%d %H:%M:%S')) # NOTE works only from 01/01/21 up to recent
df.to_csv(directory + f'\{sym}_test.csv', index=False)