n = 1000

for a in range(n):
    for b in range(n):
        for c in range(n):
            print(a, b, c)
            if a ** 2 + b ** 2 == c ** 2 and a + b + c == n and a < b < c:
                print(a, b, c, "НАЙДЕНО!")

