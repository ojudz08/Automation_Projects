python -m pip install -r requirements.txt
pyinstaller main.py --clean --onefile --name pdf_merger
python scripts/file_transfer.py