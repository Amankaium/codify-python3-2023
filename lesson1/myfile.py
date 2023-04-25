my_file = open("example.txt", 'r', encoding='utf-8')
# print(type(my_file))
# txt = my_file.read()
# print(txt)
# print(my_file)

for line in my_file:
    print(line, end="")
my_file.close()
