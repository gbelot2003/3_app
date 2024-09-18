# file_processing/excel_processor.py
import pandas as pd

def extract_text_from_excel(excel_path):
    text = ''
    xls = pd.ExcelFile(excel_path)
    for sheet_name in xls.sheet_names:
        df = xls.parse(sheet_name)
        text += df.to_string()
    return text
