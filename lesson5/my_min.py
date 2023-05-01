# функция принимает список
# и возвращает минимальной число из списка
def mad_min(lst):
    my_min = lst[0]
    for num in lst:
        if num < my_min:
            my_min = num
    return my_min

def my_sort():
    return 123

# print(__name__)
if __name__ == "__main__":
    my_lst = [0, -2, 3, -6]
    print(mad_min(my_lst))

