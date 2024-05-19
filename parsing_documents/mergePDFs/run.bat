python -m pip install -r requirements.txt
pyinstaller main.py --onefile --name pdf_merger
python move_exe.py