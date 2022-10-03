import time


def opred_2(x, y):
    matra = [[0 for j in range(2)] for i in range(2)]
    massiv = [[i[j] for j in range(len(i))] for i in a]
    for i in range(2):
        for j in range(2):
            f = False
            for k in range(n):
                for l in range(n):
                    if k != x and l != y and massiv[k][l] != False:
                        matra[i][j] = massiv[k][l]
                        massiv[k][l] = False
                        f = True
                        break
                if f == True:
                    break
    det = matra[0][0] * matra[1][1] - matra[1][0] * matra[0][1]
    return det


def matriza(massiv):
    matra = [[j for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            matra[i][j] = (-1) ** (i + j) * opred_2(i, j)
    return matra


def transponirovka(massiv):
    massa = [[0 for j in range(n)] for i in range(n)]
    for i in range(len(massiv)):
        for j in range(len(massiv[i])):
            massa[i][j] = massiv[j][i]
    return massa


def opred(massiv):
    det = 0
    for i in range(n):
        det += (-1) ** (i) * massiv[i][0] * opred_2(i, 0)
    return det


def obratnai_matriza(massiv, chizlo):
    if chizlo == 0:
        print('Найти обратную матрицу невозможно. Определитель равен 0')
    else:
        for i in range(len(massiv)):
            for j in range(len(massiv[i])):
                massiv[i][j] = round(chizlo ** (-1) * massiv[i][j], 2)
        print('Обратная матрица:')
        vivod(massiv)


def vivod(massiv):
    for i in range(len(massiv)):
        for j in range(len(massiv[i])):
            print(str(massiv[i][j]).rjust(6), end='')
        print()


def vvod(massiv):
    print('Введите значение матрицы:')
    for i in range(n):
        stroki = input().split()
        for j in range(n):
            a[i][j] = int(stroki[j])
    return a


n = 3
a = [[j for j in range(n)] for i in range(n)]
a = vvod(a)

start = time.time()
obratnai_matriza(transponirovka(matriza(a)), opred(a))
end = time.time()

print('Время жизни программы:')
print(end - start)
