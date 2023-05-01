# функция принимает список
# и возвращает минимальной число из списка
def mad_min(lst):
    my_min = lst[0]
    for num in lst:
        if num < my_min:
            my_min = num
    return my_min

# функция сортировки списка
def my_sort(array):
    sorted_array = []
    for i in range(len(array)):
        new_min = mad_min(array) # 3
        sorted_array.append(new_min) # [3]
        array.remove(new_min) # [6, 8, 9]
    return sorted_array

# функция факториала числа
def factorial(num): # 5
    result = 1
    for i in range(1, num + 1):  # 1, 2, 3, 4, 5
        result = result * i # 24 * 5
    return result

def recursion_factorial(num):
    if num == 1:
        return 1
    return recursion_factorial(num-1) * num


def cherdak(var, result=[]):
    if not isinstance(var, list):
        result.append(var)
        return result  # [7]
    else:
        for element in var:
            result = cherdak(element, result)  # 1 - cherdak(7, [])  2 -  cherdak("example", [7])
        return result


# print(__name__, "13 строка my_min.py")
if __name__ == "__main__":
    my_lst = [0, -2, 3, -6]
    print(mad_min(my_lst))
