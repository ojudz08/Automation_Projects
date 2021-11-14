"""
    Author: Ojelle Rogero
    Created on: November 14, 2021
    About:
        Converts the Weekly Market Recap section of GSAM Market Monitor
        Parse each asset type and save as a data table in separate sheet
"""

import os
import tabula
import pandas as pd


class pdfConvert():

    def __init__(self, directory, file):
        self.dir = directory
        self.file = file


    def readPdf(self, box, pg, strm):
        box_fc = [box[i] * 28.28 for i in range(0, 4)]
        df = tabula.read_pdf(os.path.join(self.dir, self.file), pages=pg, area=[box_fc], output_format='dataframe', stream=strm)
        return df


    def indexReturns(self):
        df = self.readPdf([2, 0, 20, 11], 3, True)[0]
        marketType = df.columns.values[0]
        prd = df.iloc[0, :]
        period = [prd[i] for i in range(0, len(prd)) if pd.isnull(prd[i]) == False]
        idxType = df.iloc[:, 0]
        indexType = [idxType[i] for i in range(0, len(idxType)) if pd.isnull(df.iloc[:, 1][i]) == True]
        idx = df[df.iloc[:, 0].isin(indexType)].index

        data = pd.DataFrame()
        for i in range(0, len(idx)):
            if i < len(idx) - 1:
                temp1 = df[idx[i] + 1 : idx[i+1]].reset_index(drop=True)
            else:
                temp1 = df[idx[i] + 1: len(df)].reset_index(drop=True)
            temp1 = pd.concat([pd.DataFrame([marketType] * len(temp1)),
                               pd.DataFrame([indexType[i]] * len(temp1)),
                               temp1], axis=1, ignore_index=True)
            data = data.append(temp1, ignore_index=True)

        data.columns = ["Type", "Asset Type", "Indices", period[0], period[1], period[2], period[3]]
        return data


    def commodities(self):
        df = self.readPdf([20, 0, 23, 11], 3, True)[0]
        marketType = df.columns.values[0]
        prd = df.iloc[0, :]
        period = [prd[i] for i in range(0, len(prd)) if pd.isnull(prd[i]) == False]

        data =  df[1 : len(df)].reset_index(drop=True)
        data = pd.concat([pd.DataFrame([marketType] * len(data)), data], axis=1, ignore_index=True)

        data.columns = ["Asset Type", "Commodities", period[0], period[1], period[2], period[3]]
        return data


    def currencies(self):
        df = self.readPdf([23, 0, 27, 11], 3, True)[0]
        marketType = df.columns.values[0]
        prd = df.iloc[0, :]
        period = [prd[i] for i in range(0, len(prd)) if pd.isnull(prd[i]) == False]

        data = df[1: len(df)].reset_index(drop=True)
        data = pd.concat([pd.DataFrame([marketType] * len(data)), data], axis=1, ignore_index=True)

        data.columns = ["Asset Type", "Currency Pair", period[0], period[1], period[2], period[3]]
        return data


    def ratesSpreads(self):
        df = self.readPdf([2, 11, 13, 22], 3, True)[0]
        marketType = df.columns.values[0]
        prd = df.iloc[0, :]
        period = [prd[i] for i in range(0, len(prd)) if pd.isnull(prd[i]) == False]
        rtType = df.iloc[:, 0]
        rateType = [rtType[i] for i in range(0, len(rtType)) if
                     pd.isnull(df.iloc[:, 1][i]) == True]
        idx = df[df.iloc[:, 0].isin(rateType)].index

        data = pd.DataFrame()
        for i in range(0, len(idx)):
            if i < len(idx) - 1:
                temp1 = df[idx[i] + 1: idx[i + 1]].reset_index(drop=True)
            else:
                temp1 = df[idx[i] + 1: len(df)].reset_index(drop=True)
            temp1 = pd.concat([pd.DataFrame([marketType] * len(temp1)),
                               pd.DataFrame([rateType[i]] * len(temp1)),
                               temp1], axis=1, ignore_index=True)
            data = data.append(temp1, ignore_index=True)

        data.columns = ["Type", "Rate or Spread", "Items", period[0], period[1], period[2], period[3]]
        return data


    def weeklyMarketRecap(self):
        idxRet = self.indexReturns()
        comm = self.commodities()
        curr = self.currencies()
        rtSp = self.ratesSpreads()

        with pd.ExcelWriter('GSAM_Weekly_Market_Recap.xlsx') as writer:
            idxRet.to_excel(writer, sheet_name="index_returns", index=False)
            comm.to_excel(writer, sheet_name="commodities", index=False)
            curr.to_excel(writer, sheet_name="currencies", index=False)
            rtSp.to_excel(writer, sheet_name="rates_spreads", index=False)


if __name__ == '__main__':
    directory = # directory of your file
    file = r'GSAM_market_monitor_081321.pdf'

    convert = pdfConvert(directory, file)
    convert.weeklyMarketRecap()