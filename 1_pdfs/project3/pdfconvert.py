"""
    Author: Ojelle Rogero
    Created on: April 11, 2022
    About:
        Converts the sample pdf stock level report and parse all tables
"""

import os
import tabula
import pandas as pd
import PyPDF2


class pdfConvert():

    def __init__(self, filename, output):
        self.filename = filename
        self.output = output
        self.totpg = PyPDF2.PdfFileReader(open(self.filename, 'rb')).numPages

    def readPdf(self, box, pg, strm):
        box_fc = [box[i] * 28.28 for i in range(0, 4)]
        df = tabula.read_pdf(self.filename, pages=pg, area=[box_fc], output_format='dataframe', stream=strm)
        return df

    def parsePgAll(self):
        box = [[1, 0, 20, 2.8],
               [1, 2.8, 20, 6.6],
               [1, 6.6, 20, 14.8],
               [1, 14.8, 20, 18.7],
               [1, 18.7, 20, 19.5],
               [1, 19.5, 20, 23.2],
               [1, 23.2, 20, 25]]
        data = pd.DataFrame()
        for pg in range(2, self.totpg + 1):
            temp1 = pd.DataFrame()
            for i in range(0, len(box)):
                df = self.readPdf(box[i], pg, True)[0]
                temp1 = pd.concat([temp1, df], axis=1, ignore_index=True)
            data = pd.concat([data, temp1], axis=0, ignore_index=True)
        data.columns = ['Material', 'Alte Mat.Nr.', 'Bezeichnung', 'Verfügbare Menge', 'BME', 'Produkthierarchie', 'Werk']
        return data

    def save(self):
        pgAll = self.parsePgAll()

        with pd.ExcelWriter(self.output) as writer:
            pgAll.to_excel(writer, sheet_name="Sheet1", index=False)


if __name__ == '__main__':
    file_path = # path where the pdf file is saved
    out_path = # path where to save the xlsx output

    for file in os.listdir(file_path):
        convert = pdfConvert(os.path.join(file_path, file), os.path.join(out_path, file[:-4] + '.xlsx'))
        test = convert.save()
    print('Done!')