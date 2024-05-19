"""
    Author: Ojelle Rogero
    Created on: November 23, 2021
    Modified on: May 20, 2024
    About:
        Simple python script to merge pdf files into one pdf file
"""

from pathlib import Path
from pypdf import PdfWriter
import os
import tkinter as tk
from tkinter.filedialog import *
from tkinter import messagebox, simpledialog

class PDF_Merge():
    
    def create_path(self, pdf_folder):
        output_folder = os.path.join(Path(pdf_folder).parent.absolute(), "output")
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        return output_folder


    def save_as(self, output_folder):
        file_types = [('PDF Files', '*.pdf'), ('All Files', '*.*')]
        init_dir = output_folder
        save_file_as = asksaveasfilename(initialdir=init_dir, filetypes=file_types, defaultextension='.pdf', confirmoverwrite=True)
        if save_file_as is None:
            return None
        else:
            return save_file_as


    def mergeAll(self):
        """Combines all pdf and save"""

        pdf_folder = Path(open_files[0]).parent.absolute()
        output_folder = self.create_path(pdf_folder)
        merger = PdfWriter()

        for pdf in os.listdir(pdf_folder):
            merger.append(os.path.join(pdf_folder, pdf))

        merger.write(self.save_as(output_folder))
        merger.close()
        messagebox.showinfo('Done!', 'Please check output folder.')
        


    def mergePages(self, pdf_page):
        """Combines specific pdf pages and save"""
        pdf_folder = Path(open_files[0]).parent.absolute()
        output_folder = self.create_path(pdf_folder)

        merger = PdfWriter()
        pagesToMerge = pdf_page - 1


        for pdf in os.listdir(pdf_folder):
            pdf_input = os.path.join(pdf_folder, pdf)
            pdf_open = open(pdf_input, 'rb')
            merger.append(fileobj=pdf_open, pages=[pagesToMerge])
    
        merger.write(self.save_as(output_folder))
        merger.close()
        messagebox.showinfo('Done!', 'Please check output folder.')




if __name__ == '__main__':
    open_files = askopenfilenames(initialdir=Path(__file__).parents[0])
    
    if len(open_files) > 1:
        msg = messagebox.askyesnocancel('Yes|No|Cancel', 'Do you want to merge all Pages?')
        if msg == True:
            PDF_Merge().mergeAll()
        elif msg == False:
            root = tk.Tk()
            root.withdraw()
            pdf_page = simpledialog.askinteger("Input", "Page you want to merge:")

            PDF_Merge().mergePages(pdf_page)
        else:
            pass
    else:
        messagebox.showinfo('Information', 'Select multiple files to merge')
