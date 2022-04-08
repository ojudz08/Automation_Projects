"""
    Author: Ojelle Rogero
    Created on: November 23, 2021
    About:
        Merge pdf files into one file
"""

from PyPDF2 import PdfFileMerger
import os

directory = # file path of pdfs

merger = PdfFileMerger()

for file in os.listdir(directory):
    merger.append(os.path.join(directory, file))

merger.write("output_filename.pdf")
merger.close()