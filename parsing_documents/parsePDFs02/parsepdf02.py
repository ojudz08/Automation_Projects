"""
    Author: Ojelle Rogero
    Created on: April 11, 2022
    About:
        Converts the sample pdf stock level report and parse all tables
"""

from pathlib import Path
import os, sys
import tabula
import pandas as pd
import PyPDF2


class pdfConvert():

    def __init__(self, filename, output):
        self.filename = filename
        self.output = output
        self.totpg = len(PyPDF2.PdfReader(open(self.filename, 'rb')).pages)

    def readPdf(self, box, pg, strm):
        """
          Reads the table section with its designated bounding box. Parsed the table and returns a dataframe.
            :param box:
              bounding box - list; boundary box or section of the table to parse
            :param pg:
              pdf page - int; the page section of the pdf to parse
            :param strm:
              stream mode - True or False; used to parse tables with whitespaces between cells to simulate table like structure
            :return:
              returns a dataframe output
        """
        box_fc = [box[i] * 28.28 for i in range(0, 4)]
        df = tabula.read_pdf(self.filename, pages=pg, area=[box_fc], output_format='dataframe', stream=strm)
        return df

    def parsePgAll(self):
        """
          Parse all the tables within the sample stock level pdf
            :return:
              returns the combined parsed table as dataframe
        """
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
        """
          Saves output as an xlsx
        """
        pgAll = self.parsePgAll()

        with pd.ExcelWriter(self.output) as writer:
            pgAll.to_excel(writer, sheet_name="Sheet1", index=False)


if __name__ == '__main__':
    parent_dir = Path(__file__).parents[1]
    sys.path.append(parent_dir)
    
    file_path = str(parent_dir) + r"\parsePDFs01\reports"
    out_path = str(parent_dir) + r"\parsePDFs01\output"

    for file in os.listdir(file_path):
        convert = pdfConvert(os.path.join(file_path, file), os.path.join(out_path, file[:-4] + '.xlsx'))
        convert.save()
    print('Done!')