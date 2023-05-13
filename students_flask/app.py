from flask import Flask, render_template
from openpyxl import load_workbook  # библиотека для работы с excel

first_site = Flask(__name__)


@first_site.route('/')
def hello_world():
    return """
        <div>
            Hello python-3 2023!
        </div>
        <a href="https://flask-russian-docs.readthedocs.io/ru/0.10.1/">
            Документация Flask на русском.
        </a>
    """


@first_site.route('/my-code')
def my_render():
    return render_template('index.html')


@first_site.route('/students')
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


@first_site.route('/marks')
def marks():
    excel_file = load_workbook('python_students.xlsx')
    page = excel_file["Лист1"]
    students_list = page["A"]  # [Cell, Cell, ...]
    marks_list = page['B']
    result = ''
    for i in range(len(students_list)):
        student = students_list[i].value
        mark = marks_list[i].value
        result = result + f'<div>{i+1}. {student} - {mark}</div>'
    return result


if __name__ == '__main__':
    first_site.run()
