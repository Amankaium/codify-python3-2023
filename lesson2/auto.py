from openpyxl import load_workbook

excel_file = load_workbook("my_excel.xlsx")

page = excel_file["Sheet"]
models = page["A"]
prices = page["B"]
s = 0
for cell in prices:
    s += cell.value
print(s)
