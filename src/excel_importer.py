import pandas as pd
from tkinter import filedialog, messagebox

class ExcelImporter:
    def __init__(self, root, year_var, month_var):
        self.root = root
        self.year_var = year_var
        self.month_var = month_var
        self.df = None  # 用於存儲匯入的資料
        self.df_people = None  # 用於存儲人員資料

    def import_excel(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
        if not file_path:
            # 如果按取消，則不進行任何操作
            return
        if file_path:
            # 跳過前4行，從第5行開始讀取，且不將任何行設為標題
            try:
                df = pd.read_excel(file_path, skiprows=4, header=None, sheet_name=0, usecols="A:AH")
                self.df_people = pd.read_excel(file_path, skiprows=1, header=None, sheet_name=1)
            except Exception as e:
                messagebox.showerror("匯入錯誤", f"匯入 Excel 檔案時發生錯誤: {e}")
                df = pd.DataFrame()

            # 檢查是否有資料
            has_data = not df.empty

            if has_data:
                # 將 NaN 值替換成空字串
                df = df.fillna("")

                # 新增標題列
                columns = [
                    "編號", "年度", "月份", "姓名", "月薪", "加班費", "出差天數", "出差津貼",
                    "海勤天數", "海勤津貼", "廚師津貼", "獎金", "請假天数", "請假扣款", "其他應發",
                    "薪資小計", "勞保自付額", "健保自付額", "健保金額補充保費", "薪資扣繳", "海勤所得稅5%",
                    "自提勞退", "其他應扣", "應扣小計", "實領薪資", "勞保金額", "健保金額", "勞退6%金額",
                    "其他公司負擔", "單位補充保費", "保費小計", "實付總额", "備註", "密碼"
                ]
                df.columns = columns
                self.df_people.columns = ["姓名", "職位", "到職日", "扣繳方式"]

                # 將年度和月份轉換成字串格式
                df["年度"] = df["年度"].astype(str)
                df["月份"] = df["月份"].astype(str)

                self.df = df  # 存儲匯入的資料
                # 過濾資料
                return self.filter_data()

    def filter_data(self):
        if self.df is not None:
            year = self.year_var.get()
            # 將月份轉換成 "x月" 格式
            month = self.month_var.get()
            if month != "年終":
                month = f"{int(month)}月"

            filtered_df = self.df[(self.df["年度"] == year) & (self.df["月份"] == month)]
            # 結合人員資料
            final_df = pd.merge(filtered_df, self.df_people, on="姓名", how="left")

            if final_df.empty:
                messagebox.showinfo("無資料", f"沒有找到符合年份 {year} 和月份 {month} 的資料。")
                return pd.DataFrame()
            else:
                return final_df
        else:
            messagebox.showinfo("查無資料", "請匯入正確的 Excel 檔案。")