<p align="right"><a href="https://github.com/ojudz08/AutomationProjects/tree/main">Back To Main Page</a></p>


<!-- PROJECT LOGO -->
<br />
<div align="center">
<h1 align="center">PDF Parser [To be Updated]</h1>
</div>


<!-- ABOUT PROJECT -->
### About Project

This is a simple pdf parser where it:
1. Parses the Goldman Sachs Asset Management (GSAM) Weekly Market Monitoring - Index Returns, Rates & Spreads, Commodities and Currencies
2. Save the parsed table as an excel file

Raw Data Source is a pdf file type and Output Result is save as an excel file.

### What are the pre-requisites?

Run the command below to install all python dependencies.

```Python
python -m pip install -r requirements.txt
```


https://github.com/ojudz08/AutomationProjects/assets/26113813/51339386-1803-4b82-9d7d-e3f57d0ec535



### How to Use the Project

The 'reports' folder contains the GSAM_Market_Monitor pdf file.

The output will be saved under the "output" folder

```Python
if __name__ == '__main__':
    filename = # GSAM filename herre

    convert = pdfParse()
    data = convert.weeklyMarketRecap(filename)
    print("Done converting data!")

```


<p align="right"><a href="#top">Back To Top</a></p>
