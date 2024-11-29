import tkinter as tk
from tkinter import ttk
from tkinter import font

def show_data(root, df):

    # 檢查是否已經存在 Treeview
    if hasattr(root, 'data_frame'):
        # 如果已經存在，清空原本的 Treeview
        for item in root.data_frame.get_children():
            root.data_frame.delete(item)
    else:
        # 如果不存在，創建一個框架來包含 Treeview 和 Scrollbar
        frame = tk.Frame(root)
        frame.pack(pady=5, fill=tk.BOTH, expand=True)

        # 創建 Treeview
        root.data_frame = ttk.Treeview(frame)
        root.data_frame["columns"] = list(df.columns)
        root.data_frame["show"] = "headings"

        # 創建 Scrollbar 並將其與 Treeview 連接
        vsb = ttk.Scrollbar(frame, orient="vertical", command=root.data_frame.yview)
        hsb = ttk.Scrollbar(frame, orient="horizontal", command=root.data_frame.xview)
        root.data_frame.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        vsb.pack(side="right", fill="y")
        hsb.pack(side="bottom", fill="x")
        root.data_frame.pack(side="left", fill="both", expand=True)

        # 設定每個欄位的標題和寬度
        for column in root.data_frame["columns"]:
            root.data_frame.heading(column, text=column)
            if column == "備註":
                root.data_frame.column(column, anchor="center", width=200)  # 固定 "備註" 欄位寬度為 200
            else:
                root.data_frame.column(column, anchor="center", width=font.Font().measure(column) + 20)

    # 插入資料到 Treeview
    for index, row in df.iterrows():
        root.data_frame.insert("", "end", values=list(row))