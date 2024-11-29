import tkinter as tk
from src.layout import create_date_frame
from src.excel_importer import ExcelImporter

def create_gui():
    root = tk.Tk()
    root.title("Excel 匯入介面")
    root.geometry("1200x400")  # 設定介面大小

    # 建立年份和月份選擇框架(UI)
    year_var, month_var = create_date_frame(root)
    excel_importer = ExcelImporter(root, year_var, month_var)

    # 建立按鈕框架
    button_frame = tk.Frame(root)
    button_frame.pack(pady=20)

    import_button = tk.Button(button_frame, text="選擇 Excel 檔案", command=excel_importer.import_excel)
    import_button.pack(side=tk.LEFT, padx=10)

    refresh_button = tk.Button(button_frame, text="重新整理", command=excel_importer.filter_data)
    refresh_button.pack(side=tk.LEFT, padx=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()