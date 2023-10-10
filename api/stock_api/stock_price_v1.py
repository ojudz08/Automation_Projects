"""
    Author: Ojelle Rogero
    Email: ojelle.rogero@gmail.com
    Created on: February 7, 2022
    Completed on:

    Getting data from PseAPI using requests. This is version 1
    Modification: Edit changes here


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


     # Change this function, instead of saving into an excel file, save the API into a database
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

    dir = r'C:\Users\ojell\Desktop\Oj\_Thesis\Data\stock_price'
    period = ['2021-01-01', '2022-02-04']    # Add date range using format ['YYYY-MM-DD', 'YYYY-MM-DD']

    test = PseStockPrice(dir, period)

    print(test.pseFile())
