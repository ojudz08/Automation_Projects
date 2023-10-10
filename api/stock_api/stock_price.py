"""
    Author: Ojelle Rogero
    Email: ojelle.rogero@gmail.com
    Created on: August 4, 2021
    Completed on: August 9, 2021

    Getting data from PseAPI using requests.

"""

import requests
import pandas as pd
import os

class PseStockPrice():

    def __init__(self, directory, period):
        self.dir = directory
        self.pse = 'pse_company_all.xls'
        self.api_url = r'https://pselookup.vrymel.com/api'
        self.period = period


    def pseFile(self):
        file = os.path.join(self.dir, self.pse)
        if os.path.exists(file):
            output = pd.read_excel(file)
        else:
            output = f"Check if {self.pse} exist"

        return output

    def pseAPI(self):
        df = self.pseFile()
        data = df.copy()    #Remove .head() once you've created the error function

        symbol = data['Stock Symbol']
        df_all = pd.DataFrame()
        for i in range(0, len(data)):
            response = requests.get(self.api_url + f'/stocks/{symbol[i]}/history/{self.period[0]}/{self.period[1]}')
            api = pd.DataFrame(response.json()['history'])
            comp = pd.concat([pd.DataFrame(data.iloc[i, :]).T] * len(api), ignore_index=True)
            comb_data = pd.concat([comp, api], axis=1)

            df_all = df_all.append(comb_data)

        df_all.to_csv(self.dir + r'\pse_stock_price_all.csv', index=False)

        msg = "Done pulling out data!"

        return msg


if __name__ == "__main__":

    # Add path variable where to save the file
    # Add date range using format ['YYYY-MM-DD', 'YYYY-MM-DD']

    test = PseStockPrice(path, period)
    print(test.pseAPI())