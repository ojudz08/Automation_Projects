<!-- PROJECT LOGO -->
<br />
<div align="center">
<h1 align="center">Data Profiler</h1>
</div>


<!-- ABOUT PROJECT -->
### About Project

Data profiling is the process of checking what your data looks like for data quality analysis. This is a simple data profiler script where source is a csv file and outputs a xlsx file.

Raw Data Source is in csv file type.

Output Result is save a xlsx file type.

1. Data Shape

2. Column Profile

3. Data Statistics

4. Column Distinct Values


https://github.com/ojudz08/AutomationProjects/assets/26113813/add56f0b-02ca-46fb-b015-94b447584ead


<p align="right">(<a href="#top">back to top</a>)</p>

### What are the pre-requisites?

There's no necessary third party libraries used. You only need the pandas library for this project. Run the command below to install all python dependencies.

```Python
python -m pip install -r requirements.txt
```



<p align="right">(<a href="#top">back to top</a>)</p>

### How to Use the Project

Modify the following:
- src_folder
- output_folder
- output_filename

NOTE: You can opt and create your own folder names and filename.

```Python
if __name__ == "__main__":
    src_folder = # folder name where your source data is
    output_folder = # folder name where you want to save your output
    output_filename = "data_profile_output.xlsx" # you can name whatever your output file name is

    data = dataProfiler(src_folder, output_folder, output_filename).saveResultToExcel()   

```
<p align="right">(<a href="#top">back to top</a>)</p>

