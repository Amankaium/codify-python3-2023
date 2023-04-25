def my_function(num):
    dels = []

    for i in range(1, num):
        if num % i == 0:
            dels.append(i)

    sr_ar = sum(dels) / len(dels)

    return dels, sr_ar

print(my_function(18))
