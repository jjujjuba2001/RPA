import openpyxl as op

wb = op.Workbook()
ws = wb.create_sheet ("지출내역서")

print(ws)
ws = wb["지출내역서"]

title = ["날짜","항목","가격","인원","총 가격(단가*인원)"]
ws.append (title)

data = [['2022-07-01', '다과비', 5000,3],
        ['2022-07-02', '점심 식대', 10000,2],
        ['2022-07-02', '저녁 식대', 13000,1],
        ['2022-07-03', '유류비', 100000,3],
        ['2022-07-04', 'coffee', 15000,5],
        ['2024-07-12', '가나다', 254000,2]]

for cell_data in data:
    ws.append (cell_data)

#ws["C8"] = "=sum(C2:C7)"

row_max = ws.max_row
col_max = ws.max_column

print("로우 최대값 : ", row_max)
print("컬럼 최대값 : ", col_max)

for row_max in range (2, row_max+1):
    print(row_max)
    ws.cell(row_max,col_max).value = "=C"+ str(row_max) + "*" + "D"+ str(row_max)
    row_max -= 1
    print(row_max)
    
wb.save (r"C:\Users\user\Documents\Code\지출내역서.xlsx")


                    
wb.close()
                     
