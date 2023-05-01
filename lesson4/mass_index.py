# написать функцию для определения индекса массы
# тела, то есть функция принимает 2 числа:
# рост в метрах и вес в кг
# вес надо разделить на квадрат роста
# полученное число и есть индекс массы
# его надо вернуть через return

def find_mass_index(height, weight):
    index = weight / (height ** 2)
    print(index)
    return index

# print(find_mass_index(1.7, 60))
def another_function():
    print("this is another sparta")
    find_mass_index(1.7, 60)

def third():
    another_function()
    find_mass_index(1.7, 60)
    # third()


third()
