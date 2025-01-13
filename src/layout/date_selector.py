import tkinter as tk
from datetime import datetime

def create_date_frame(root):
    current_year = datetime.now().year
    # 獲取上個月的月份，如果當前月份是 1 月，則上個月為 12 月
    previous_month = datetime.now().month - 1 if datetime.now().month > 1 else 12

    date_frame = tk.Frame(root)
    date_frame.pack(pady=5)  # 設定框架的外邊距

    # 建立並配置年份標籤
    year_label = tk.Label(date_frame, text="選擇年份")
    year_label.grid(row=0, column=0, padx=5)  # 設定標籤的位置和內邊距
    year_var = tk.StringVar(root)  # 建立一個字串變數來儲存選擇的年份
    # 建立年份選項列表，包含去年、今年和明年
    year_options = [str(year) for year in range(current_year - 1, current_year + 2)]
    # 根據上個月的月份來預選年份
    if previous_month == 12:
        year_var.set(str(current_year - 1))  # 如果上個月是 12 月，預選去年
    else:
        year_var.set(str(current_year))  # 否則預選今年
    # 建立年份選單並配置其位置
    year_menu = tk.OptionMenu(date_frame, year_var, *year_options)
    year_menu.grid(row=0, column=1, padx=5)

    # 建立並配置月份標籤
    month_label = tk.Label(date_frame, text="選擇月份")
    month_label.grid(row=0, column=2, padx=5)  # 設定標籤的位置和內邊距
    month_var = tk.StringVar(root)  # 建立一個字串變數來儲存選擇的月份
    # 建立月份選項列表，包含 1 到 12 月
    month_options = [str(month) for month in range(1, 13)]
    month_options.append("年終")  # 在月份選項中加入"年終"選項
    month_var.set(str(previous_month))  # 預選上個月
    # 建立月份選單並配置其位置
    month_menu = tk.OptionMenu(date_frame, month_var, *month_options)
    month_menu.grid(row=0, column=3, padx=5)

    return year_var, month_var