import sys, os

ocrselector = ['pytesseract']
translator_selector = ['google']
app_name = "Japan OCR"
app_ver = "0.5a"
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
dicdir = os.path.join(base_path, 'unidic', 'dicdir')
capture_prompt = "<div style=\"display: flex; justify-content: center; align-items: center; height: 100vh;\"><p style=\"margin: 0;\">Click the Capture button or use Alt + Q</p></div>"