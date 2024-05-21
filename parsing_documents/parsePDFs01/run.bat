python -m pip install -r requirements.txt
pyinstaller main.py --onefile --name pdf_parser
python move_exe.py