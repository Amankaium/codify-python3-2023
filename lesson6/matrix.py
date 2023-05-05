from my_min import cherdak
m = [
    [4,     7,      8],
    [7,	    23,	    63],
    [72,	63,	    5],
    [5,	    0,	    3],
]

# напишите функцию, которая прнимает двумерный массив
# и возвращает все элементы в одномерном
# [4, 7, 8, 7, 23, 63, 72, 63, 5, 5, 0, 3]

def make_flat(matrix):
    r = []
    for lst in matrix:  # lst == [4,     7,      8]
        for element in lst:  # element == 4
            r.append(element)
    return r

def make_flat_2(matrix):
    r = []
    for i in range(len(matrix)):  #
        # print(matrix[i])
        for j in range(len(matrix[i])):
            r.append(matrix[i][j])
    return r

print(make_flat(m))
print(make_flat_2(m))
print(cherdak(m))
print(m[1][2])  # [7, 23, 63]

img = [
    [[255, 255, 255], [255, 0, 0]],
    [[0, 0, 255], [0, 0, 0]]
]
