"""
    Author: Ojelle Rogero
    Created on: September 21, 2023
    Modified on: 
    About:
        <ADD ABOUT HERE>
    Modification / Updates:
        <>
"""

from pathlib import Path
import os, sys
import tabula
import pandas as pd


class pdfParse():

    def __init__(self, filename):
        parent_dir = Path(__file__).parents[0]
        sys.path.append(parent_dir)

        self.filename = os.path.join(parent_dir, "reports", filename)
        self.output = os.path.join(parent_dir, "output")


    def readPdf(self, box, pg, strm):
        box_fc = [box[i] * 28.28 for i in range(0, 4)]
        df = tabula.read_pdf(self.filename, pages=pg, area=[box_fc], output_format='dataframe', stream=strm)
        return df
    
    def getIndex(self):
        idx = []
        for pg in range(1, 5):
            temp = self.readPdf([2, 0, 27, 4.4], pg, True)[0]
            for rw in range(0, len(temp)):
                try:
                    int(temp.iloc[rw, 0].replace(',', ''))
                    idx.append(rw)
                    break
                except:
                    pass 
        return idx
    
    
    def commonStocks(self):
        # [2, 0, 27, 4.4]  
        idx = self.getIndex()
        temp = self.readPdf([2, 0, 27, 15], 4, True)[0]
        return temp.iloc[5:,:].reset_index(drop=True)
    



if __name__ == '__main__':
    filename = r"pdftest.pdf"

    convert = pdfParse(filename)
    data = convert.commonStocks()
    print(data)
