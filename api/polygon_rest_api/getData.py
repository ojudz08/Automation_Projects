"""
    Author: Ojelle Rogero
    Email: ojelle.rogero@gmail.com
    Created on: April 10, 2023
    Completed on: 
    Getting TRON data from Polygon.io API.
"""

import config
import os, json, requests, time
from datetime import datetime, timedelta
import pandas as pd

class CryptoData():

    def __init__(self, pair, date_range):
        self.cur_dir = os.getcwd()
        self.pair_frm = pair[0]
        self.pair_to = pair[1]
        self.pair = f'{pair[0]}-{pair[1]}'
        self.date_frm = date_range[0]
        self.date_to = date_range[1]
        self.api_url = r'https://api.polygon.io/v1'

    def open_close(self):
        # check if pair folder exists, if not create
        # Comment: try-except, create if not exist
        open_close_fp = self.cur_dir + f'\open_close_data\{self.pair}'
        if not os.path.isdir(open_close_fp):
            os.mkdir(open_close_fp)

        dt_start = datetime.strptime(self.date_frm, "%Y-%m-%d")
        dt_end = datetime.strptime(self.date_to, "%Y-%m-%d")
        dt_diff = abs(dt_end - dt_start).days + 1
        
        for i in range(0, dt_diff):
            dt = dt_start + timedelta(days = i)
            
            # get data on weekdays only
            if dt.weekday() < 5:
                dt_as_of = dt.strftime("%Y-%m-%d")
                data = requests.get(f'{self.api_url}/open-close/crypto/{self.pair_frm}/{self.pair_to}/{dt_as_of}?adjusted=true&apiKey={config.api_key}')
                
                if data.status_code == 200:
                    filepath = open_close_fp + f'\{dt_as_of}.json'
                    with open(filepath, "w") as fp:
                        json.dump(data.json(), fp, indent=4)
                else: # if API calls exceed 5 where response!=200, wait 65 sec before proceeding
                    time.sleep(65)                
            else:
                pass
        return "Done data requests!"
    
    def transformData(self):
        open_close_fp = self.cur_dir + f'\open_close_data\{self.pair}'
        data_li = []
        for file in os.listdir(open_close_fp):
            with open(os.path.join(open_close_fp, file), "r") as f:
                data = json.load(f)        
            data_li.append(data)

        df = pd.DataFrame.from_records(data_li, columns=["symbol", "day", "open", "close"])
        df["day"] = pd.to_datetime(df["day"]).dt.tz_localize(None)
        df = df.set_index("day")
        df.reset_index(drop=True)

        dt_frm = datetime.strptime(self.date_frm, "%Y-%m-%d").strftime("%m%d%y")
        dt_to = datetime.strptime(self.date_to, "%Y-%m-%d").strftime("%m%d%y")
        df.to_csv(f'{self.pair}_{dt_frm}_{dt_to}.csv')
        return "Done transforming, data saved!"


if __name__ == "__main__":
    pair = ["TRX", "USD"]
    date_range = ["2023-01-01", "2023-05-19"]
    
    tronData = CryptoData(pair, date_range)
    data = tronData.open_close()
    print(data)

    etl = tronData.transformData()
    print(etl)

