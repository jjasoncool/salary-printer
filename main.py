import tkinter as tk
from src.layout import create_date_frame, show_data
from src.excel_importer import ExcelImporter
from src.pdf_generator import PDFGenerator

def show_treeview(root, excel_importer, refresh=False):
    if refresh:
        filtered_df = excel_importer.filter_data()
    else:
        filtered_df = excel_importer.import_excel()

    show_data(root, filtered_df)

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

    import_button = tk.Button(button_frame, text="選擇 Excel 檔案", command= lambda: show_treeview(root, excel_importer))
    import_button.pack(side=tk.LEFT, padx=10)

    refresh_button = tk.Button(button_frame, text="重新整理", command= lambda: show_treeview(root, excel_importer, refresh=True))
    refresh_button.pack(side=tk.LEFT, padx=10)

    pdf_button = tk.Button(button_frame, text="產生 PDF", command=PDFGenerator.generate)
    pdf_button.pack(side=tk.LEFT, padx=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()