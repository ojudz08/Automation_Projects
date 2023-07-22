"""
    Author: Ojelle Rogero
    Created on: November 23, 2021
    Modified on: July 22, 2023
    About:
        Simple python script to merge pdf files into one pdf file
"""

from pathlib import Path
from pypdf import PdfWriter
import os, sys

class PDF_Merge():

    def __init__(self, pdf_folder, output_folder, output_filename):
        self.pdf_folder = pdf_folder
        self.output_folder = output_folder
        self.output_filename = output_filename
    

    def mergeAll(self):
        """Combines all pdf and save"""
        merger = PdfWriter()

        for pdf in os.listdir(self.pdf_folder):
            merger.append(os.path.join(self.pdf_folder, pdf))

        merger.write(os.path.join(self.output_folder, self.output_filename))
        merger.close()


    def mergePages(self, pagesToMerge):
        """Combines specific pdf pages and save"""
        merger = PdfWriter()
        pagesToMerge = pagesToMerge -1

        for pdf in os.listdir(self.pdf_folder):
            pdf_input = os.path.join(self.pdf_folder, pdf)
            pdf_open = open(pdf_input, 'rb')
            merger.append(fileobj=pdf_open, pages=[pagesToMerge])
    
        output_file = os.path.join(self.output_folder, self.output_filename)
        output = open(output_file, "wb")
        merger.write(output)

        merger.close()
        output.close()


if __name__ == '__main__':
    parent_dir = Path(__file__).parents[1]
    sys.path.append(parent_dir)

    pdf_folder =  str(parent_dir) + r"\mergePDFs\reports"
    output_folder =  str(parent_dir) + r"\mergePDFs\output"
    merged_filename = r"Nasdaq_Commodities_Summary.pdf"
    merged_1stpages = r"Nasdaq_Commodities_Market_Report.pdf"

    pdfAll = PDF_Merge(pdf_folder, output_folder, merged_filename)
    pdfAll.mergeAll()
    print("Done merging all pdfs!")

    pdfpages = PDF_Merge(pdf_folder, output_folder, merged_1stpages)
    pdfpages.mergePages(pagesToMerge=1)
    print("Done merging 1st pages of the pdfs!")