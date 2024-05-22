python -m pip install -r requirements.txt
pyinstaller main.py --clean --onefile --name pdf_parser
python scripts/file_transfer.py