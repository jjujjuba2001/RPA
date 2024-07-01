import openpyxl as op

wb = op.Workbook()
ws = wb.create_sheet ("지출내역서")

print(ws)
ws = wb["지출내역서"]

title = ["날짜","항목","가격"]
ws.append (title)

data = [['2022-07-01', '다과비', 5000],
        ['2022-07-02', '점심 식대', 10000],
        ['2022-07-02', '저녁 식대', 13000],
        ['2022-07-03', '유류비', 100000],
        ['2022-07-04', 'coffee', 15000]
        ['2024-07-12', '가나다', 254000]]

for cell_data in data:
    ws.append (cell_data)

ws["C7"] = "=sum(C2:C6)"

ws = wb.active

wb.save (r"C:\Users\user\Documents\Code\지출내역서.xlsx")


                    
wb.close()
                     
