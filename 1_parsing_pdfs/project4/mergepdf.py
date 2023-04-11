"""
    Author: Ojelle Rogero
    Created on: November 23, 2021
    About:
        Simple python script to merge pdf files into one pdf file
"""

from PyPDF2 import PdfMerger
import os

class pdfMerge():

    def __init__(self, file, output):
        self.file = file
        self.output = output

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
    file_path =  # path where the pdf file is saved
    out_path =  # path where to save the combined pdfs
    output_file =  # combined pdf output file name

    mergepdf = pdfMerge(file_path, os.path.join(out_path, output_file))
    mergepdf.merge()
    print('Done merging all pdfs!')