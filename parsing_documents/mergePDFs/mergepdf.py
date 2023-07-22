"""
    Author: Ojelle Rogero
    Created on: November 23, 2021
    Modified on: July 22, 2023
    About:
        Simple python script to merge pdf files into one pdf file
"""

from pathlib import Path
from PyPDF2 import PdfMerger
import os, sys

class pdfMerge():

    def __init__(self, file, output):
        self.file = file
        self.output = outputPdfMerger

    def merge(self):
        """
          Combines all pdf and save
        """
        merger = PdfMerger()
        for pdf in os.listdir(self.file):
            if pdf[-3:] == 'pdf': merger.append(os.path.join(self.file, pdf))
        merger.write(self.output)
        merger.close()


if __name__ == '__main__':
    parent_dir = Path(__file__).parents[1]
    sys.path.append(parent_dir)

    file_path =  str(parent_dir) + r"\mergePDFs\reports"
    out_path =  str(parent_dir) + r"\mergePDFs\output"
    output_file =  "Nasdaq_Commodities_Summary.pdf"

    mergepdf = pdfMerge(file_path, os.path.join(out_path, output_file))
    mergepdf.merge()
    print('Done merging all pdfs!')
