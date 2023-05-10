from flask import Flask, render_template
from openpyxl import load_workbook  # библиотека для работы с excel

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello python-3 2023!"

@app.route('/my-code')
def my_render():
    return render_template('index.html')

@app.route('/students')
def students():
    students_list = []
    my_file = load_workbook("python_students.xlsx")  # открываем файл через его путь
    page = my_file["Лист1"]  # обращаемся к нужной страница по имени
    students_cells = page["A"]  # берём список ячеек по имени колонны
    for cell in students_cells:
        students_list.append(cell.value)
    result = ""
    for index, student in enumerate(students_list):  # 0, "Elver"
        result += f"<div>{index+1}. {student}</div>"
    return result

if __name__ == '__main__':
    app.run()
