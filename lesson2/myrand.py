from openpyxl import Workbook

my_excel = Workbook()
my_page = my_excel.active
my_page["C2"] = "Ранен"

my_excel.save("my_excel.xlsx")
