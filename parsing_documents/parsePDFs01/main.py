"""
    Author: Ojelle Rogero
    Created on: November 14, 2021
    Updated on: May 21, 2024
    About:
        Converts the Weekly Market Recap section of GSAM Market Monitor
        Parse each asset type and save as a data table in separate sheet
    Modification / Updates:
        Function definition, input and output parameters are added.
"""

import os, sys, logging
import tabula
import pandas as pd
import tkinter as tk
from tkinter.filedialog import *
from tkinter import messagebox


root = logging.getLogger()
root.setLevel(logging.DEBUG)
class pdfParse():

    def __init__(self):
        self.init_dir = os.path.abspath(os.path.dirname(sys.argv[0]))

    def open_file(self):
        """Open the file"""
        open_file = askopenfilenames(initialdir=self.init_dir)
        return open_file


    def save_as(self):
        """Save the pdf result to desired target folder"""
        file_types = [('Excel Files', '*.xlsx'), ('All Files', '*.*')]
        save_file_as = asksaveasfilename(initialdir=self.init_dir, filetypes=file_types, defaultextension='.xlsx', confirmoverwrite=True)
        if save_file_as is None:
            return None
        else:
            return save_file_as


    def readPdf(self, filepath, box, pg, strm):
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
        df = tabula.read_pdf(filepath, pages=pg, area=[box_fc], output_format='dataframe', stream=strm)
        return df


    def getIndex(self, filepath):
        """ Gets the index of each asset type"""
        df1 = self.readPdf(filepath, [2, 0, 27, 11], 3, True)[0]
        df2 = self.readPdf(filepath, [2, 11, 13, 22], 3, True)[0]
        assetCol1, assetCol2 = df1.iloc[:,0], df2.iloc[:,0]
        asset = ["EQUITIES", "FIXED INCOME", "OTHER", "RATES", "SPREADS"]
        idx = [assetCol1[assetCol1 == asset[0]].index[0], 
               assetCol1[assetCol1 == asset[1]].index[0],
               assetCol1[assetCol1 == asset[2]].index[0],
               assetCol2[assetCol2 == asset[3]].index[0],
               assetCol2[assetCol2 == asset[4]].index[0]]
        return idx


    def indexReturns(self, filepath):
        """
          Parse the Index Returns table (page 3 of the pdf)
            :input   None, Input df is called from readPdf function
            :output  data - Index Returns output as dataframe
        """
        df = self.readPdf(filepath, [2, 0, 20, 11], 3, True)[0]
        idx = self.getIndex(filepath)
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

        data.columns = ["Type", "Asset Type", "Index"] + df.iloc[0, 1:5].values.tolist()
        return df



    def commodities(self, filepath):
        """
          Parse the Commodities table (page 3 of the pdf)
            :input   None, Input df is called from readPdf function
            :output  data - Commodities Returns output as dataframe
        """
        df = self.readPdf(filepath, [20, 0, 23, 11], 3, True)[0]
        commodities_df = df.iloc[1: len(df)].reset_index(drop=True)
        temp1_df = pd.DataFrame({0: ["COMMODITIES"] * len(commodities_df)})
        data = pd.concat([temp1_df, commodities_df], axis=1, ignore_index=True)

        data.columns = ["Asset", "Commodities"] + df.iloc[0, 1:5].values.tolist()
        return data


    def currencies(self, filepath):
        """
          Parse the Currencies table (page 3 of the pdf)
            :input   None, Input df is called from readPdf function
            :output  data - Currencies Returns output as dataframe
        """
        df = self.readPdf(filepath, [23, 0, 27, 11], 3, True)[0]
        fx_df = df.iloc[1: len(df)].reset_index(drop=True)
        temp1_df = pd.DataFrame({0: ["CURRENCIES"] * len(fx_df)})
        data = pd.concat([temp1_df, fx_df], axis=1, ignore_index=True)

        data.columns = ["Asset", "FX Pair"] + df.iloc[0, 1:5].values.tolist()
        return data


    def ratesSpreads(self, filepath):
        """
          Parse the Rates & Spreads table (page 3 of the pdf)
            :input   None, Input df is called from readPdf function
            :output  data - Rates or Spreads output as dataframe
        """
        df = self.readPdf(filepath, [2, 11, 13, 22], 3, True)[0]
        idx = self.getIndex(filepath)[-2:]
        asset = ["RATES", "SPREADS"]
        
        data = pd.DataFrame()
        for i in range(0, 2):
            if i == 1: idx_n = len(df)
            else: idx_n = idx[i + 1] 

            ratesSpreads_df = df.iloc[idx[i] + 1: idx_n, :].reset_index(drop=True)
            temp1_df = pd.DataFrame({0: ["Rates & Spreads"] * len(ratesSpreads_df), 
                                     1: [asset[i]] * len(ratesSpreads_df)})
            temp2_df = pd.concat([temp1_df, ratesSpreads_df], axis=1, ignore_index=True)
            data = pd.concat([data, temp2_df], ignore_index=True)       

        data.columns = ["Asset", "Rates or Spreads", "Asset Name"] + df.iloc[0, 1:5].values.tolist()   
        return data


    def weeklyMarketRecap(self):
        """
          Saves output as an xlsx
            :input   None. Inputs are from the multiple asset classs function
            :output  Outputs as xls file
        """
        filepath = os.path.abspath(self.open_file()[0])
        filename = os.path.basename(filepath)

        print(f"Parsing {filename}...")
        print("This will take at least 1-2 mins..")
        idxRet = self.indexReturns(filepath)
        comm = self.commodities(filepath)
        curr = self.currencies(filepath)
        rtSp = self.ratesSpreads(filepath)

        output_file = self.save_as()

        with pd.ExcelWriter(output_file) as writer:
            idxRet.to_excel(writer, sheet_name="index_returns", index=False)
            comm.to_excel(writer, sheet_name="commodities", index=False)
            curr.to_excel(writer, sheet_name="currencies", index=False)
            rtSp.to_excel(writer, sheet_name="rates_spreads", index=False)

        

if __name__ == '__main__':
    pdfParse().weeklyMarketRecap()

    messagebox.showinfo("Show Info", "Done converting data!") 
