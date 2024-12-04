import os, sys
import platform
import subprocess

# 檢查 LibreOffice 是否安裝
def check_libreoffice_installed():
    system = platform.system()
    if system == "Windows":
        command = ["where", "/R", "C:\\Program Files", "soffice"]
    else:
        command = ["which", "soffice"]

    try:
        subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except subprocess.CalledProcessError:
        return False


def get_real_output_dir(output_subdir="output"):
    """
    動態取得輸出目錄，根據運行環境決定
    :param output_subdir: 相對輸出資料夾名稱
    :return: 絕對路徑
    """
    # 如果是 PyInstaller 打包後的執行檔
    if getattr(sys, 'frozen', False):
        # 獲取執行檔所在目錄
        base_dir = os.path.dirname(sys.executable)
    else:
        # 獲取原始碼所在目錄
        base_dir = os.path.dirname(sys.argv[0])

    # 建立輸出目錄
    output_dir = os.path.join(base_dir, output_subdir)
    os.makedirs(output_dir, exist_ok=True)  # 如果資料夾不存在則建立
    return output_dir