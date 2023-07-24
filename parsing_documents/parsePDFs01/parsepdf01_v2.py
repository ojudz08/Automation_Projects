"""
    Author: Ojelle Rogero
    Created on: November 14, 2021
    Modified on: July 22, 2023
    About:
        Converts the Weekly Market Recap section of GSAM Market Monitor
        Parse each asset type and save as a data table in separate sheet
    Modification / Updates:
        Function definition, input and output parameters are added.
"""

from pathlib import Path
import pandas as pd
import os, sys
from pypdf import PdfWriter, PdfReader






parent_dir = Path(__file__).parents[1]
sys.path.append(parent_dir)

pdf_folder =  str(parent_dir) + r"\parsePDFs01\reports"
output_folder =  str(parent_dir) + r"\parsePDFs01\output"
pdf_filename = r"GSAM_Market_Monitor_081222.pdf"
output_filename = r"GSAM_Weekly_Market_Recap.xlsx"

    
read_pdf = PdfReader(os.path.join(pdf_folder, pdf_filename))
totpage = len(read_pdf.pages) 

third_page = read_pdf.pages[2]
extracted = third_page.extract_text()


idx_ret = ['Equities', 'Fixed Income', 'Other']
idx_ret_lower = [item.lower() for item in idx_ret]

to_save_in = os.path.join(output_folder, 'test.txt')
with open(to_save_in, 'w') as f:
    f.write(extracted)


df = pd.read_csv(to_save_in, sep='\t', encoding='unicode_escape', engine='python')


for row in df.iloc[:, 0]:
    newstr = row.replace("%", "")
    try:
        print(float(newstr))
        # append to each column -- 1 week, MTD, QTD, YTD
    except:
        print(f"{newstr} - Not a float")
        # append to first column -- Equities, Fixed Income, Other


