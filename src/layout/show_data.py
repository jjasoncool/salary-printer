import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import font

def show_data(root, df):

    # 創建一個框架來包含 Treeview 和 Scrollbar
    frame = tk.Frame(root)
    frame.pack(pady=5, fill=tk.BOTH, expand=True)

    # 創建 Treeview
    data_frame = ttk.Treeview(frame)
    data_frame["columns"] = list(df.columns)
    data_frame["show"] = "headings"

    # 設定每個欄位的標題和寬度
    for column in data_frame["columns"]:
        data_frame.heading(column, text=column)
        if column == "備註":
            data_frame.column(column, anchor="center", width=200)  # 固定 "備註" 欄位寬度為 200
        else:
            data_frame.column(column, anchor="center", width=font.Font().measure(column) + 20)

    # 插入資料到 Treeview
    for index, row in df.iterrows():
        data_frame.insert("", "end", values=list(row))

    # 創建 Scrollbar 並將其與 Treeview 連接
    vsb = ttk.Scrollbar(frame, orient="vertical", command=data_frame.yview)
    hsb = ttk.Scrollbar(frame, orient="horizontal", command=data_frame.xview)
    data_frame.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    vsb.pack(side="right", fill="y")
    hsb.pack(side="bottom", fill="x")
    data_frame.pack(side="left", fill="both", expand=True)
