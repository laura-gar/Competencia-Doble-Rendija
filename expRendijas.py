from sys import stdin
import Graficas


def action(matriz, vector):
    v = [0 for i in range(len(matriz))]
    for i in range(len(matriz)):
        for j in range(len(vector)):
            v[i] += round(matriz[i][j] * vector[j],2)
    return v


def matrizProbabilities(slits, targets):
    dim = slits + targets + 1
    matriz = [[0.0 for j in range(dim)] for i in range(dim)]
    # loop
    for i in range(slits + 1, dim):
        matriz[i][i] = 1.0

    # slits
    for i in range(1, slits + 1):
        matriz[i][0] = round(1 / slits, 3)

    # targets
    j = 1
    i = slits + 1
    if slits%2 == 0:
        m1 = (targets + 1) //2
        m2 = m1 - m1 //2
    else:
        m1 = targets  // 2
        m2 = m1 - m1 // 2

    while i <= len(matriz) - m1 and j < slits + 1:
        for k in range(i,  i + m1):
            matriz[k][j] = round(1 / (m1), 2)
        i = i + m2
        j += 1

    return matriz


def pp(matriz):
    for i in range(len(matriz)):
        print(matriz[i], sep='\n')


def expRendijas(slits, targets, clicks):
    matriz_proba = matrizProbabilities(slits, targets)
    print('Matriz de probabilidad')
    pp(matriz_proba)
    state = [1] + [0 for i in range(slits + targets)]
    for i in range(clicks):
        state = action(matriz_proba,state)
    return state


