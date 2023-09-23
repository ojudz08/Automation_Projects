"""
    Author: Ojelle Rogero
    Created on: September 21, 2023
    Modified on: 
    About:
        This is an ongoing project....
    Modification / Updates:
        <>
"""

from pathlib import Path
import os, sys
import tabula
from PyPDF2 import PdfReader
import pandas as pd


class pdfParse():

    def __init__(self, filename):
        parent_dir = Path(__file__).parents[0]
        sys.path.append(parent_dir)

        self.filename = os.path.join(parent_dir, "reports", filename)
        self.output = os.path.join(parent_dir, "output")


    def readPdf(self, box, pg, strm):
        #[box[i] * 28.28 for i in range(0, 4)]
        box_fc = [box[i] * 25 for i in range(0, 4)]
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
        temp = self.readPdf([2, 0, 27, 22], 4, True)[0]
        return temp.iloc[5:,:].reset_index(drop=True)
    
    def test(self):
        reader = PdfReader(self.filename)
        num_pgs = len(reader.pages)
        page = reader.pages[3]
        text = page.extract_text()
        return text
    

    def savetoExel(self):
        data = pd.DataFrame([self.test()])

        output_file = os.path.join(self.output, 'test.xlsx')
        with pd.ExcelWriter(output_file) as writer:
            data.to_excel(writer, sheet_name="test", index=False)



if __name__ == '__main__':
    filename = r"pdftest.pdf"

    convert = pdfParse(filename)
    data = convert.savetoExel()
    #print("pdf converted")
    print(data)
