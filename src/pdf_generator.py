import sys, os, platform
import tkinter as tk
import json
import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Alignment
from PyPDF2 import PdfReader, PdfWriter

from src.utility import check_libreoffice_installed, get_real_output_dir

class PDFGenerator:
    @staticmethod
    def load_mapping():
        base_path = os.path.dirname(__file__)
        file_path = os.path.join(base_path, "..", "mapping.json")
        with open(file_path, "r", encoding="utf-8") as file:
            mapping = json.load(file)
        return mapping

    @staticmethod
    def generate(df):
        root_path = os.path.dirname(os.path.dirname(__file__))
        template_path = os.path.join(root_path, "templates/salary_form.xlsx")
        output_dir = get_real_output_dir("output")
        mapping = PDFGenerator.load_mapping()

        # print(df)

        for index, row in df.iterrows():
            this_month = row["月份"]
            file_name = f"{row["年度"]}-{row["月份"]}_{row["姓名"]}"
            workbook = load_workbook(template_path)
            sheet = workbook.active
            # 公司名稱
            if "comp_name" in mapping:
                sheet["A2"] = mapping["comp_name"]
            else:
                print("Key 'comp_name' not found in mapping")
            # 其他資料處理
            # 加密密碼
            print(row.iloc[33], row["密碼"])
            # 扣繳方式
            # TODO: 扣繳方式不同需要修改df的數值
            print(row.iloc[36], row["扣繳方式"])
            print(row.iloc[32], row["備註"])

            for map_item in mapping["mapping"]:
                if "df_column" in map_item:
                    # 獲取欄位索引
                    columns = map_item["df_column"]
                    # 找 mapping 的設定資料
                    if map_item.get("operation") == "sum":
                        column_values = row.iloc[columns]
                        column_values = column_values.apply(lambda x: 0 if pd.isna(x) or x == "" else x)
                        value = "{:,}".format(int(column_values.sum()))
                        print(value)
                    else:
                        # Perform operation if specified
                        if row.iloc[map_item["df_column"]] != "":
                            # 依據資料格式轉換
                            data_type = map_item.get("data_type")
                            if data_type == "date":
                                value = pd.to_datetime(
                                    row.iloc[map_item["df_column"]]
                                ).strftime("%Y-%m-%d")
                            elif data_type == "string":
                                value = str(row.iloc[map_item["df_column"]]).replace("\\n", "\n")
                            else:
                                value = "{:,}".format(int(row.iloc[map_item["df_column"]]))
                        else:
                            value = ""
                    # 填入欄位
                    cell = sheet[map_item["xlsx_cell"]]
                    cell.value = "" if str(value) == "0" else value

                    # 如果 value 包含換行符號，設定 wrap_text 屬性
                    if data_type == "string":
                        if "\n" in value:
                            cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)

            # Save the Excel file path
            xlsx_output_path = os.path.join(
                output_dir, f'{file_name}.xlsx'
            )
            # Save the PDF file path
            pdf_output_path = os.path.join(
                output_dir, f'{file_name}.pdf'
            )

            try:
                workbook.save(xlsx_output_path)
            except PermissionError:
                tk.messagebox.showerror("錯誤", f"無法寫入 {xlsx_output_path}，請關閉該 Excel 檔案後重試。")
                return

            # load LibreOffice
            print(f"Opening {xlsx_output_path}")
            if not check_libreoffice_installed():
                raise EnvironmentError("LibreOffice is not installed or not found in system PATH.")
            else:
                if platform.system() == "Windows":
                    convert_command = f'start /wait "" "soffice" --headless --convert-to pdf "{xlsx_output_path}" --outdir "{output_dir}"'
                    # convert_command = f'start soffice --calc "{xlsx_output_path}"'
                else:
                    convert_command = f'soffice --headless --convert-to pdf "{xlsx_output_path}" --outdir "{output_dir}"'
                # subprocess.run(convert_command, check=True)
                try:
                    os.system(convert_command)
                except PermissionError:
                    tk.messagebox.showerror("錯誤", f"無法寫入 {pdf_output_path}，請關閉該 PDF 檔案後重試。")
                    return

            # 加密處理
            with open(pdf_output_path, 'rb') as pdf_file:
                reader = PdfReader(pdf_file)
                writer = PdfWriter()
                writer.append_pages_from_reader(reader)
                writer.encrypt(user_password=row["密碼"], owner_pwd=row["密碼"], use_128bit=True)

                with open(pdf_output_path, 'wb') as encrypted_pdf_file:
                    writer.write(encrypted_pdf_file)

            print(f"Encrypted PDF generated at {pdf_output_path}")

            print("-----------------")

        tk.messagebox.showinfo("提示", f"{this_month}薪資檔案已經產生在 {os.path.abspath(output_dir)} 資料夾。")
