# Напишите функцию,
# которая будет
# отрисовывать полный
# треугольник
def full_triangle(n):
    print(" " * n, "*")
    for i in range(n):
        spaces_outside = n - i
        spaces_inside = i * 2 + 1
        print(f"{spaces_outside * ' '}*{spaces_inside * ' '}*")
    print("* " * round(n * 1.5))


def write_letter(letter):
    if letter == "c":
        print("""
######
#       
#
#
######
""")
    elif letter == "b":
        print("""
######
#   #    
###
#   #
######
       """)


write_letter("b")
write_letter("c")
# full_triangle(6)
