result = {}


def take_input(student_id, *args):
    result[student_id] = list(*args)


while True:
    my_input = input()  # "Nazima_Iminova 85 23 69 45 17"

    if my_input == "finish":
        break

    lst = my_input.split()  # ['Nazima_Iminova', '85', '23' ...]
    student_name = lst[0]
    marks = lst[1:]
    take_input(student_name, marks)

print(result)
