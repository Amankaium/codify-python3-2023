n = 100

def sum_sq(n):
    r = 0
    for i in range(1, n+1):
        sq = i * i
        r += sq

    return r

def sq_of_sum(n):
    return sum(list(range(1, n+1))) ** 2

print(sq_of_sum(n) - sum_sq(n))
