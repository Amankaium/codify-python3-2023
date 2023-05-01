# Создать бесконечный цикл, для ввода и
# добавления чисел в список numbers
# пока не будет введено число 0
numbers = []
while True:
    a = int(input("Введите число для добавления: "))
    if a == 0:
        break
    numbers.append(a)
print("Список:", numbers)

# Найти максимальное число из списка numbers,
# не используя функции max, sort
numbers = [7, 34, -6, 8]
dragon = numbers[0]
for num in numbers:
    if num > dragon:
        dragon = num
print(dragon)


# Из numbers получить список more_ten
# только числа в нём должны быть больше 10
# more_ten = []
# for num in numbers:
#     if num > 10:
#         more_ten.append(num)
