<p align="right"><a href="https://github.com/ojudz08/AutomationProjects/tree/main">Back To Main Page</a></p>


<!-- PROJECT LOGO -->
<br />
<div align="center">
<h1 align="center">PDF Parser</h1>
</div>


<!-- ABOUT PROJECT -->
### About Project

This is a simple pdf parser where it:
1. Parses the GSAM Assets from pdf into a summary 
   - Index Returns
   - Rates & Spreads
   - Commodities
   - Currencies
2. Save each asset type into a separate sheet

### What are the requirements?
1. Download jdk 8 from the archive downloads (this [link](https://www.oracle.com/in/java/technologies/javase/javase8-archive-downloads.html) )
2. Install the jdk 8.
3. Set your JAVA_HOME to the path where your jdk 8 is installed. 
   ```
   C:\Program Files\Java\jdk-1.8
   ```
4. Add these to your environment variable
   ```
   C:\Program Files\Java\jdk-1.8
   C:\Program Files\Java\jdk-1.8\bin
   ```
5. Download the tabula-jar dependency from this [link](https://github.com/tabulapdf/tabula-java/releases). Then save it within the JAVA_HOME\jre\lib

6. Add the path to your environment variable
   ```
   JAVA_HOME\jre\lib\{tabula-jar-dependency}
   ```

### What are the pre-requisites?

Run the command below in following order. Or you may simply run the run.bat which also contains the commands below.

```Python
python -m pip install -r requirements.txt
pyinstaller main.py --clean --onefile --name pdf_parser
python scripts/file_transfer.py
```

### Running the Script
1. Save your reports within __*reports*__ folder.

2. This will install all the necessary python libraries used.
   ```Python
   python -m pip install -r requirements.txt
   ```

3. Create an executable file pdf_parser.exe from the main.py
   ```Python
   pyinstaller main.py --clean --onefile --name pdf_parser
   ```

4. Move the created executable file in the current directory.
   ```Python
   python scripts/file_transfer.py
   ```

### How to use pdf_parser
1. After running the script above, you will see a **_pdf_parser_** application.

2. Once you run the application, it will prompt you to open the file.

   ![alt text](img/image1.png)
   
3. Wait for the parsing to be completed.

   ![alt text](img/image2.png)

4. Once parsing has been completed, it will prompt you to save the file.

   ![alt text](img/image3.png)

   ![alt text](img/image4.png)

   ![alt text](img/image5.png)



<!-- CONTACT -->
### Disclaimer

This project was created using Windows, the run.bat will only work with Windows. Please contact Ojelle Rogero - ojelle.rogero@gmail.com for any questions with email subject "Github Parsing PDFs".
