import pandas as pd
from tkinter import filedialog, messagebox
from src.layout import show_data

def import_excel(root, year_var, month_var):
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
    if file_path:
        df = pd.read_excel(file_path, skiprows=4, header=None)  # 跳過前4行，從第5行開始讀取，且不將任何行設為標題
        # 檢查是否有資料
        has_data = not df.empty

        if has_data:
            # 將 NaN 值替換成空字串
            df = df.fillna("")

            # 新增標題列
            columns = ["編號", "年度", "月份", "姓名", "月薪", "加班費", "出差天數", "出差津貼", "海勤天數", "海勤津貼", "廚師津貼", "獎金", "請假天数", "請假扣款", "薪資小計", "勞保自付額", "健保自付額", "健保金額補充保費", "薪資扣繳", "海勤所得稅5%", "自提勞退", "自付小計", "實領薪資", "勞保金額", "健保金額", "勞退6%金額", "單位補充保費", "保費小計", "實付總额", "備註", "密碼"]
            df.columns = columns

            # 打印每個欄位的資料類型
            print("資料類型:")
            print(df.dtypes)

            # 將年度和月份轉換成字串格式
            df["年度"] = df["年度"].astype(str)
            df["月份"] = df["月份"].astype(str)

            year = year_var.get()
            # 將月份轉換成 "x月" 格式
            month = f"{int(month_var.get())}月"

            filtered_df = df[(df["年度"] == year) & (df["月份"] == month)]

            if filtered_df.empty:
                messagebox.showinfo("無資料", f"沒有找到符合年份 {year} 和月份 {month} 的資料。")
            else:
                show_data(root, filtered_df)
                messagebox.showinfo("匯入成功", "Excel 檔案已成功匯入並顯示。")