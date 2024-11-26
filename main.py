import tkinter as tk
from src.excel_importer import import_excel
from datetime import datetime

def create_gui():
    root = tk.Tk()
    root.title("Excel 匯入介面")
    root.geometry("400x300")  # 設定介面大小

    year_label = tk.Label(root, text="選擇年份")
    year_label.pack(pady=5)
    year_var = tk.StringVar(root)
    current_year = datetime.now().year
    year_options = [str(year) for year in range(current_year - 1, current_year + 2)]
    year_menu = tk.OptionMenu(root, year_var, *year_options)
    year_menu.pack(pady=5)

    month_label = tk.Label(root, text="選擇月份")
    month_label.pack(pady=5)
    month_var = tk.StringVar(root)
    month_options = [str(month) for month in range(1, 13)]
    month_menu = tk.OptionMenu(root, month_var, *month_options)
    month_menu.pack(pady=5)

    import_button = tk.Button(root, text="選擇 Excel 檔案", command=import_excel)
    import_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_gui()