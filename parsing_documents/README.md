<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/ojudz08/Projects/tree/main/1_pdfs">
    <img src="images/logo.jpg" alt="Logo" width="45" height="50">
  </a>

<h2 align="center">Parsing/Merging PDFs</h2>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#about-each-project">About Each Project</a></li>
	  <li><a href="#limitations">Limitations</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

Contains multiple projects on parsing pdfs into an excel output, merging and converting pdfs.

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- INSTALLATION -->
## Installation

Install the necessary libraries and/or prerequisites before using the python script/s.

* [pandas](https://pandas.pydata.org/docs/user_guide/index.html)
   ```sh
   pip install pandas
   ```
* [tabula-py](https://pypi.org/project/tabula-py/)
  ```sh
   pip install tabula-py
  ```
* [pypdf](https://pypi.org/project/pypdf/)
  ```sh
   pip install pypdf
  ```
  For using pypdf with AES encryption or decryption, install extra dependencies:
  ```sh
   pip install pypdf[crypto]
  ```
* [PyCryptodome](https://pypi.org/project/pycryptodome/)
  ```sh
   pip install PyCryptodome
  ```

NOTE: If you're familiar with using conda install, please see the links below:

* [Installing Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html#)
* [conda install](https://docs.conda.io/projects/conda/en/latest/commands/install.html)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- USAGE -->
## Usage

```python
import os
import tabula
import PyPDF2
import pandas as pd

if __name__ == '__main__':
    file_path = r"\path\where the pdf file is saved"
    input_file = r"pdf_filename.pdf"
    out_path = r"\path\where to save the xlsx output"
    output_file = r"output_filename.xlsx"

```

Make sure to modify the file path; filename of the input file; output path; and filename of the output file within the main function before running the script.

Each of these libraries here can do a lot more. Please see the documentation for each to explore examples.

* [os](https://docs.python.org/3/library/os.html#)
* [tabula](https://tabula-py.readthedocs.io/en/latest/tabula.html#)
* [PyPDF2](https://pypi.org/project/PyPDF2/)
* [pandas](https://pandas.pydata.org/docs/)


<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ABOUT EACH PROJECT EXAMPLES -->
## About Each Project

<br />
<p align="left">Project 1: Parse the index returns, commodities, currencies and rate spreads of Goldman Sachs Asset Management Market Monitor report and save each parsed column in each excel tab.</p>
<div align="left">
  <a href="https://github.com/ojudz08/Projects/tree/main/1_pdfs">
    <img src="images/input_output_prj1.jpg" alt="Project_1" width="900" height="450">
  </a>
</div>

<br /><br />
<p align="left">Project 2: Parse the columns of stock level pdf and convert into excel file.</p>
<div align="left">
  <a href="https://github.com/ojudz08/Projects/tree/main/1_pdfs">
    <img src="images/input_output_prj2.jpg" alt="Project_2" width="900" height="450">
  </a>
</div>

<br /><br />
<p align="left">Project 3: Similar to project 2, parse the tables of the first 3 pages of sample pdf report then convert to excel file.</p>
<div align="left">
  <a href="https://github.com/ojudz08/Projects/tree/main/1_pdfs">
    <img src="images/input_output_prj3.jpg" alt="Project_3" width="900" height="450">
  </a>
</div>

<br /><br />
<p align="left">Project 4: Merge pdf reports</p>
<div align="left">
  <a href="https://github.com/ojudz08/Projects/tree/main/1_pdfs">
    <img src="images/input_output_prj4.jpg" alt="Project_4" width="600" height="300">
  </a>
</div>

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LIMITATIONS -->
## Limitations

The python script here parse or converts the specified pdf reports. It may or may not work on all formats. Please contact the author for any suggestions or recommendations on these projects.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Ojelle Rogero - ojelle.rogero@gmail.com with email subject "Github Parsing PDFs"

<p align="right">(<a href="#top">back to top</a>)</p>
