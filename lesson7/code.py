def half_triangle(n):
    print("*")
    for i in range(n):  # 0 -> n   0 1 2 3 4
        print(f"*{' ' * i}*")
    print("* " * round(n * 0.7))


n = 12  # берём значения до 12
half_triangle(n)


