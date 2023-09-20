"""
    Author: Ojelle Rogero
    Created on: November 14, 2021
    Modified on: September 14, 2023
    About:
        Converts the Weekly Market Recap section of GSAM Market Monitor
        Parse each asset type and save as a data table in separate sheet
    Modification / Updates:
        Function definition, input and output parameters are added.
"""

from pathlib import Path
import os, sys
import tabula
import pandas as pd
import numpy as np


class pdfParse():

    def __init__(self, report_folder, output_folder, filename):
        parent_dir = Path(__file__).parents[0]
        sys.path.append(parent_dir)

        self.filename = os.path.join(parent_dir, report_folder, filename)
        self.output = os.path.join(parent_dir, output_folder)


    def readPdf(self, box, pg, strm):
        """
          Reads the table section with its designated bounding box. Parsed the table and returns a dataframe.
            :input
              box  --> bounding box - list; boundary box or section of the table to parse
              pg   --> pdf page - int; the page section of the pdf to parse
              strm --> stream mode - True or False; used to parse tables with whitespaces between cells to simulate table like structure
            :output
              df   --> parsed and converted content from pdf output as dataframe
        """
        box_fc = [box[i] * 28.28 for i in range(0, 4)]
        df = tabula.read_pdf(self.filename, pages=pg, area=[box_fc], output_format='dataframe', stream=strm)
        return df

    def getIndex(self):
        df1 = self.readPdf([2, 0, 27, 11], 3, True)[0]
        df2 = self.readPdf([2, 11, 13, 22], 3, True)[0]
        assetCol1, assetCol2 = df1.iloc[:,0], df2.iloc[:,0]
        asset = ["EQUITIES", "FIXED INCOME", "OTHER", "COMMODITIES", "CURRENCIES", "RATES", "SPREADS"]
        idx = [assetCol1[assetCol1 == asset[0]].index[0], 
               assetCol1[assetCol1 == asset[1]].index[0],
               assetCol1[assetCol1 == asset[2]].index[0],
               assetCol1[assetCol1 == asset[3]].index[0],
               assetCol1[assetCol1 == asset[4]].index[0],
               assetCol2[assetCol2 == asset[5]].index[0],
               assetCol2[assetCol2 == asset[6]].index[0],]
        return idx

    def indexReturns(self):
        """
          Parse the Index Returns table (page 3 of the pdf)
            :input   None, Input df is called from readPdf function
            :output  data - Index Returns manipulated table output as dataframe
        """
        df = self.readPdf([2, 0, 20, 11], 3, True)[0]
        idx = self.getIndex()
        asset = ["EQUITIES", "FIXED INCOME", "OTHER"]
        
        data = pd.DataFrame()
        for i in range(0, 3):
            if i == 2: idx_n = len(df)
            else: idx_n = idx[i + 1] 

            indexRet_df = df.iloc[idx[i] + 1: idx_n, :].reset_index(drop=True)
            temp1_df = pd.DataFrame({0: ["Index Returns"] * len(indexRet_df), 
                                     1: [asset[i]] * len(indexRet_df)})
            temp2_df = pd.concat([temp1_df, indexRet_df], axis=1, ignore_index=True)
            data = pd.concat([data, temp2_df], ignore_index=True)       

        data.columns = ["Type", "Asset Type", "Index", "1 week", "MTD", "QTD", "YTD"]
        
        return data


    def commodities(self):
        """
          Parse the Commodities table (page 3 of the pdf)
            :input   None, Input df is called from readPdf function
            :output  data - Commodities Returns manipulated table output as dataframe
        """
        df = self.readPdf([20, 0, 23, 11], 3, True)[0]
        commodities_df = df.iloc[1: len(df)].reset_index(drop=True)
        temp1_df = pd.DataFrame({0: ["COMMODITIES"] * len(commodities_df)})
        data = pd.concat([temp1_df, commodities_df], axis=1, ignore_index=True)
        
        data.columns = ["Asset", "Commodities"] + df.iloc[0, 1:5].values.tolist()

        return data


    def currencies(self):
        """
          Parse the Currencies table (page 3 of the pdf)
            :input
              None. Input df is called from readPdf function
            :output
              data - currencies manipulated table output as dataframe
        """
        df = self.readPdf([23, 0, 27, 11], 3, True)[0]
        marketType = df.columns.values[0]
        prd = df.iloc[0, :]
        period = [prd[i] for i in range(0, len(prd)) if pd.isnull(prd[i]) == False]

        data = df[1: len(df)].reset_index(drop=True)
        data = pd.concat([pd.DataFrame([marketType] * len(data)), data], axis=1, ignore_index=True)

        data.columns = ["Asset Type", "Currency Pair", period[0], period[1], period[2], period[3]]
        return data


    def ratesSpreads(self):
        """
          Parse the Rates & Spreads table (page 3 of the pdf)
            :input
              None. Input df is called from readPdf function
            :output
              data - rates or spreads manipulated table output as dataframe
        """
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
        """
          Saves output as an xlsx
            :input
              None. Inputs are from the multiple asset classs function
            :output
              outputs an xls file
        """
        idxRet = self.indexReturns()
        comm = self.commodities()
        curr = self.currencies()
        rtSp = self.ratesSpreads()

        with pd.ExcelWriter(self.output) as writer:
            idxRet.to_excel(writer, sheet_name="index_returns", index=False)
            comm.to_excel(writer, sheet_name="commodities", index=False)
            curr.to_excel(writer, sheet_name="currencies", index=False)
            rtSp.to_excel(writer, sheet_name="rates_spreads", index=False)


if __name__ == '__main__':
    
    report_folder = "reports"
    output_folder = "output"
    filename = r"GSAM_Market_Monitor_081222.pdf"

    convert = pdfParse(report_folder, output_folder, filename)
    test = convert.commodities()
    print(test)
