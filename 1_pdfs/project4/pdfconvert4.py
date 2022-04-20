"""
    Author: Ojelle Rogero
    Created on: April 20, 2022
    About:
        Parses the tables in the first 3 pages of sample pdf report and save output as xlsx.
"""

import os
import tabula
import pandas as pd


class pdfConvert():

    def __init__(self, filename, output):
        self.filename = filename
        self.output = output

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
        box = [[3.5, 0, 13, 20],
               [3, 0, 13, 20],
               [2.5, 0, 13, 20]]
        data = pd.DataFrame()
        for i in range(0, 3): #self.totpg + 1
            temp1 = pd.DataFrame()
            pg = i + 1
            df = self.readPdf(box[i], pg, True)[0]
            temp1 = pd.concat([temp1, df], axis=1, ignore_index=True)
            data = pd.concat([data, temp1], axis=0, ignore_index=True)
        data.columns = ['Gemeinde / GB Nr.', 'Fläche in m2', 'Beschrieb (ME Miteigentums-Anteil; (STWE Stockwerkeigentums-Wertquote',
                        'Name/Wohnort/Sitz Veräusserer', 'Name/Wohnort/Sitz Erwerber', 'Erwerb durch Veräusserer']
        return data

    def save(self):
        """
          Saves output as an xlsx
        """
        pgAll = self.parsePgAll()

        with pd.ExcelWriter(self.output) as writer:
            pgAll.to_excel(writer, sheet_name="Sheet1", index=False)


if __name__ == '__main__':
    file_path = # path where the pdf file is saved
    out_path = # path where to save the xlsx output

    for file in os.listdir(file_path):
        convert = pdfConvert(os.path.join(file_path, file), os.path.join(out_path, file[:-4] + '.xlsx'))
        convert.save()
    print('Done!')