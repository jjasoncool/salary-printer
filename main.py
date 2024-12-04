import tkinter as tk
from src.layout import create_date_frame, show_data
from src.excel_importer import ExcelImporter
from src.pdf_generator import PDFGenerator

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

def show_treeview(root, excel_importer, refresh=False):
    if refresh:
        filtered_df = excel_importer.filter_data()
    else:
        filtered_df = excel_importer.import_excel()

    show_data(root, filtered_df)

def generate_pdf(root, excel_importer):
    df = excel_importer.filter_data()
    if show_data(root, df):
        PDFGenerator.generate(df)

def create_gui():
    root = tk.Tk()
    root.title("Excel 匯入介面")
    root.geometry("1200x400")  # 設定介面大小

    center_window(root)

    # 建立年份和月份選擇框架(UI)
    year_var, month_var = create_date_frame(root)

    # 建立 Excel 匯入器
    excel_importer = ExcelImporter(root, year_var, month_var)

    # 建立按鈕框架
    button_frame = tk.Frame(root)
    button_frame.pack(pady=20)

    import_button = tk.Button(button_frame, text="選擇 Excel 檔案", command= lambda: show_treeview(root, excel_importer))
    import_button.pack(side=tk.LEFT, padx=10)

    refresh_button = tk.Button(button_frame, text="檢視資料", command= lambda: show_treeview(root, excel_importer, refresh=True))
    refresh_button.pack(side=tk.LEFT, padx=10)

    def show_loading():
        loading_window = tk.Toplevel(root)
        loading_window.title("Loading")
        loading_window.geometry("200x100")

        center_window(loading_window)

        tk.Label(loading_window, text="正在產生 PDF...").pack(pady=20)
        return loading_window

    def generate_pdf_and_close_loading(loading_window):
        generate_pdf(root, excel_importer)
        loading_window.destroy()

    def generate_pdf_with_loading():
        loading_window = show_loading()
        root.after(100, lambda: generate_pdf_and_close_loading(loading_window))

    pdf_button = tk.Button(button_frame, text="產生 PDF", command=generate_pdf_with_loading)
    pdf_button.pack(side=tk.LEFT, padx=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()