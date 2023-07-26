"""
    Author: Ojelle Rogero
    Email: ojelle.rogero@gmail.com
    Created on: April 10, 2023
    Modified on: July 25, 2023
    Completed on: 
    Getting TRON data from Polygon.io API.
"""

import config
import os, sys, json, requests, time
from pathlib import Path
from datetime import datetime, timedelta
import pandas as pd

class CryptoData():

    def __init__(self, pair, date_range):
        self.api_url = r'https://api.polygon.io'
        self.project_dir = Path(__file__).parents[0]
        self.pair_frm = pair[0]
        self.pair_to = pair[1]
        if len(date_range) == 1:
            self.date_frm = date_range[0]
        else:
            self.date_frm = date_range[0]
            self.date_to = date_range[1]

    
    def ohlc_allCryptoMarket(self):
        dt_start = datetime.strptime(self.date_frm, "%Y-%m-%d")
        dt_end = datetime.strptime(self.date_to, "%Y-%m-%d")
        dt_diff = abs(dt_end - dt_start).days + 1

        # Initialize empty dataframe
        result_df = pd.DataFrame()

        # Set counter to pause if requests reaches 5
        counter = 0
        for i in range(0, dt_diff):
            counter = counter + 1
            if counter == 5:
                time.sleep(65)
                counter = 0

            dt_1 = dt_start + pd.Timedelta(days = i)
            date = dt_1.strftime("%Y-%m-%d")

            if dt_1.weekday() < 5:
                url = f"{self.api_url}/v2/aggs/grouped/locale/global/market/crypto/{date}?adjusted=true&apiKey={config.api_key}"
                request_data = requests.get(url)
            
                crypto_df = pd.DataFrame(request_data.json()['results'])
                crypto_df = crypto_df.rename(columns={"T": "Crypto Pair",
                                                      "v": "Volume",
                                                      "vw": "Volume Weighted Ave Price",
                                                       "o": "Open",
                                                       "c": "Close",
                                                       "h": "High",
                                                       "l": "Low",
                                                       "t": "Timestamp (Unix Msec)",
                                                       "n": "Num of Transactions"}, errors="raise")

                data_df = pd.concat([pd.DataFrame([date] * len(crypto_df), columns=["Date"]), crypto_df], axis=1)
            
                result_df = pd.concat([result_df, data_df], axis=0)
            else:
                pass
        
        # Save to csv
        result_df.to_csv(f"{self.project_dir}\ohlc_data\{self.date_frm}_{self.date_to}.csv", index=False)
        
        return result_df
        
    

if __name__ == "__main__":
    pair = ["TRX", "USD"]
    date_range = ["2023-01-01", "2023-07-21"]
    
    tronData = CryptoData(pair, date_range)
    data = tronData.ohlc_allCryptoMarket()
    print(data)