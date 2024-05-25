# Reference
# https://towardsdev.com/6-python-packages-for-working-with-pdf-files-fab9065ae24d

# Libraries to check
# PyPDF2

import os
import tabula
import csv

directory = r'C:\Users\ojell\Desktop\Oj\_Projects\pdftoexcel'

for filename in os.listdir(directory):
    if filename.endswith(".pdf"):
        print(filename[:-4])
        tabula.convert_into(os.path.join(directory, filename), os.path.join(directory, filename[:-4]) + ".csv", output_format="csv", pages="all")
