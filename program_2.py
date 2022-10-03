import numpy as nm


def create_filled_matrix(values, string_count, column_count):
    matrix = nm.zeros((string_count, column_count))
    for n in range(string_count):
        for m in range(column_count):
            matrix[n][m] = values[n * column_count + m]

    return matrix


def create_user_matrix():
    strings = int(input("Количество строк: "))
    columns = int(input("Количество столбцов: "))
    values = [int(input(">")) for i in range(strings * columns)]
    return create_filled_matrix(values, strings, columns)


action = int(input("Действие; 1. Транспонировать 2. Умножить 3. Ранг: "))

if action == 1:
    print(create_user_matrix().transpose())
elif action == 2:
    m1 = create_user_matrix()
    m2 = create_user_matrix()
    print(m1 * m2)
elif action == 3:
    print(nm.linalg.matrix_rank(create_user_matrix()))