<p align="right"><a href="https://github.com/ojudz08/AutomationProjects/tree/main">Back To Main Page</a></p>


<!-- PROJECT LOGO -->
<br />
<div align="center">
<h1 align="center">PDF Merger</h1>
</div>


<!-- ABOUT PROJECT -->
### About Project

This is a project where it:
1. Merge all the pdf pages
2. Merge only the 1st pdf page

Raw Data Source is a pdf file type and Output Result is save as a pdf file type as well.

### What are the pre-requisites?

Run the command below to install all python dependencies.

```Python
python -m pip install -r requirements.txt
```


https://github.com/ojudz08/AutomationProjects/assets/26113813/6a024d59-ba34-46e5-9c6f-4d43b2d7a704


### How to Use the Project

Under the 'reports' folder, add the necessary pdf you want to merge.

Rename the following, as you see fit.
- merged_filename
- merged_1stpages

NOTE: If you want to the merged files for the pdf file, you may comment the 2nd merged filename.

```Python
if __name__ == '__main__':
    parent_dir = Path(__file__).parents[1]
    sys.path.append(parent_dir)

    pdf_folder =  str(parent_dir) + r"\mergePDFs\reports"
    output_folder =  str(parent_dir) + r"\mergePDFs\output"
    merged_filename = # filename of the merged pdf pages
    merged_1stpages = # filename of the merged 1st pdf pages

    pdfAll = PDF_Merge(pdf_folder, output_folder, merged_filename)
    pdfAll.mergeAll()
    print("Done merging all pdfs!")

    pdfpages = PDF_Merge(pdf_folder, output_folder, merged_1stpages)
    pdfpages.mergePages(pagesToMerge=1)
    print("Done merging 1st pages of the pdfs!")

```


<p align="right"><a href="#top">Back To Top</a></p>
