import pandas as pd
from tkinter import filedialog, messagebox

def import_excel(skiprows=4):
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
    if file_path:
        df = pd.read_excel(file_path, skiprows=skiprows)  # 跳過前skiprows行，從第skiprows+1行開始讀取
        print(df)
        messagebox.showinfo("匯入成功", "Excel 檔案已成功匯入並顯示在控制台。")