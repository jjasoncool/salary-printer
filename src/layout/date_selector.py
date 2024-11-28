import tkinter as tk
from datetime import datetime

def create_date_frame(root):
    current_year = datetime.now().year
    previous_month = datetime.now().month - 1 if datetime.now().month > 1 else 12

    date_frame = tk.Frame(root)
    date_frame.pack(pady=5)

    year_label = tk.Label(date_frame, text="選擇年份")
    year_label.grid(row=0, column=0, padx=5)
    year_var = tk.StringVar(root)
    year_options = [str(year) for year in range(current_year - 1, current_year + 2)]
    if previous_month == 12:
        year_var.set(str(current_year - 1))  # 預選現在年份 - 1
    else:
        year_var.set(str(current_year))  # 預選現在年份
    year_menu = tk.OptionMenu(date_frame, year_var, *year_options)
    year_menu.grid(row=0, column=1, padx=5)

    month_label = tk.Label(date_frame, text="選擇月份")
    month_label.grid(row=0, column=2, padx=5)
    month_var = tk.StringVar(root)
    month_options = [str(month) for month in range(1, 13)]
    month_var.set(str(previous_month))  # 預選上個月
    month_menu = tk.OptionMenu(date_frame, month_var, *month_options)
    month_menu.grid(row=0, column=3, padx=5)

    return year_var, month_var