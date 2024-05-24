# Reference
# https://enjoymachinelearning.com/blog/extract-data-from-pdf-python/

# Libraries to check
# PyPDF2
# pdfplumber
# Camelot
# pdfminer.six

import os
import tabula
import csv

directory = r'C:\Users\ojell\Desktop\Oj\_Projects\pdftoexcel'

for filename in os.listdir(directory):
    if filename.endswith(".pdf"):
        print(filename[:-4])
        tabula.convert_into(os.path.join(directory, filename), os.path.join(directory, filename[:-4]) + ".csv", output_format="csv", pages="all")
