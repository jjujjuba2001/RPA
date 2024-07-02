import openpyxl as op
import win32com.client

excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True

path = r"C:\Users\user\Documents\Code\지출내역서.xlsx"

wb = op.load_workbook(path, data_only = True)
ws = wb["지출내역서"]

data = []

for row in ws.rows:
    data.append(row[4].value)

print (data)

temp_wb = excel.Workbooks.Open(r"C:\Users\user\Documents\Code\지출내역서.xlsx")
temp_wb.Save()
temp_wb.Close()