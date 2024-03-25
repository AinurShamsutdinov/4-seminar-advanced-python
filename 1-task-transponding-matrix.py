# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

#transposed_matrix = transpose(matrix)

# Введите ваше решение ниже

DEFAULT_VALUE = 0


def transpose(matrix):
    trans = list()

    for i in range(len(matrix[0])):
        init_list = list()
        for k in range(len(matrix)):
            init_list.append(DEFAULT_VALUE)
        trans.append(init_list)

    for i in range(len(matrix)):
        for k in range(len(matrix[i])):
            trans[k][i] = matrix[i][k]
    return trans


def print_matrix(trans):
    print('*****************')
    for l_print in trans:
        print(l_print)
    print('*****************')


print_matrix(matrix)
trans_matrix = transpose(matrix)
print_matrix(trans_matrix)
