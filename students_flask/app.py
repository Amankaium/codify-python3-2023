from flask import Flask, render_template, request
from openpyxl import load_workbook  # библиотека для работы с excel

app = Flask(__name__)


@app.route('/')
def hello_world():
    return """
        <nav>
            <ul>
                <li><a href="/">Домой</a></li>
                <li><a href="/my-code">Мой код</a></li>
                <li><a href="/add">Добавить студента</a></li>
            </ul>
        </nav>
        <div>
            Hello python-3 2023!
        </div>
        <a href="https://flask-russian-docs.readthedocs.io/ru/0.10.1/">
            Документация Flask на русском.
        </a>
    """


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


@app.route('/marks')
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


@app.route('/add', methods=["GET", "POST"])
def add_student():
    data = request.form  # dictionary
    # print(data)
    if data:
        new_student = data["student_name"]
        mark_1 = int(data["mark_1"])
        mark_2 = int(data["mark_2"])
        excel_file = load_workbook('python_students.xlsx')
        page = excel_file["Лист1"]
        page.append([new_student, mark_1, mark_2])
        excel_file.save('python_students.xlsx')
        return f"Вы добавили {new_student}!"
    return render_template('create_student.html')


if __name__ == '__main__':
    app.run()
