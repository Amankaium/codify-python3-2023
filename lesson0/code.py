# [5, 25, 15, 36, 382, 35, 100, 0, 1]
# делятся на 3: 15 36
# делятся на 5: 5 25 15 100

lst = [5, 25, 15, 36, 382, 35, 100, 0, 1, 3.1, "test"]

for num in lst:
    if num != 0 and num.isdigit():
        if num % 3 == 0:
            print("На 3: ", num)
        if num % 5 == 0:
            print("На 5: ", num)

# for num in lst:
#     if num % 3 == 0 and num != 0:
#         print("На 3: ", num)
#     if num % 5 == 0 and num != 0:
#         print("На 5: ", num)
