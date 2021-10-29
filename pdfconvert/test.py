import os
from pathlib import Path
import tabula
import csv


class pdfConvert():

    def __init__(self, directory):
        self.dir = directory

    def readPdf(self):
        #scale = [box[i] * 28.28 for i in range(0, 4)]
        df = tabula.read_pdf(Path(self.dir))
        return df

    def box(self):
        pass

if __name__ == 'main':
    directory = r'C:\Users\ojell\Desktop\Oj\_Projects\pdftoexcel2\GSAM_market_monitor_081321.pdf'

    convert = pdfConvert(directory)
    test = convert.readPdf()

    print(test)