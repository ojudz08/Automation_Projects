<p align="right"><a href="https://github.com/ojudz08/AutomationProjects/tree/main">Back To Main Page</a></p>


<!-- PROJECT LOGO -->
<br />
<div align="center">
<h1 align="center">PDF Merger</h1>
</div>


<!-- ABOUT PROJECT -->
### About

This is a project where it:
1. Merge all the pdf pages
2. Merge only the 1st pdf page

Raw Data Source is a pdf file type and Output Result is save as a pdf file type as well.

### What are the pre-requisites?

Run the command below in following order.

```Python
python -m pip install -r requirements.txt
pyinstaller main.py --onefile --name pdf_merger
python move_exe.py
```

Or you may simply run the run.bat


https://github.com/ojudz08/AutomationProjects/assets/26113813/6a024d59-ba34-46e5-9c6f-4d43b2d7a704


### Running the Script
1. Save your reports within __*reports*__ folder.

2. This will install allthe necessary python libraries used.
   ```Python
   python -m pip install -r requirements.txt
   ```

3. Create an executable file pdf_merger.exe from the main.py
   ```Python
   pyinstaller main.py --onefile --name pdf_merger
   ```

4. Move the created executable file in the current directory.
   ```Python
   python move_exe.py
   ```


<!-- CONTACT -->
### Disclaimer

This project was created using Windows, the run.bat will only work with Windows. Please contact Ojelle Rogero - ojelle.rogero@gmail.com for any questions with email subject "Github Parsing PDFs".
