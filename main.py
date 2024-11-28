import tkinter as tk
from src.excel_importer import import_excel
from src.layout.date_selector import create_date_frame

def create_gui():
    root = tk.Tk()
    root.title("Excel 匯入介面")
    root.geometry("1200x400")  # 設定介面大小

    create_date_frame(root)

    import_button = tk.Button(root, text="選擇 Excel 檔案", command=lambda: import_excel(root))
    import_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_gui()