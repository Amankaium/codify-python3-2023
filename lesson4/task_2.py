profile = {
    "name": "Kaium",
    "surname": "Amanbaev",
    "second_name": "Amanbaev",
}
# Бесконечный ввод двух слов: ключа и значения
# через пробел в одну строку
# если ключ в словаре уже есть, то цикл прекращается
# проверка ключа: x in profile
# если ключа в словаре нет, то ключ и значение добавляется
while True:
    pair = input()  # "language python"
    lst = pair.split()
    if len(lst) == 2:
        key, value = lst  # ["language", "python"]
        if key in profile:
            break
        profile[key] = value
    else:
        print("Нужно ввести 2 слова через пробел")
print(profile)
