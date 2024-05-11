def radixsort(lista, k):
    for i in range(0, k):
        lista = counting(lista, 9, i)
    return lista


def counting(lista, m, c):
    n = len(lista)
    f = [0] * (m + 1)
    y = [0] * (n + 1)

    for i in range(1, n + 1):
        j = (lista[i - 1] // 10 ** c) % 10
        f[j] += 1

    for i in range(1, m + 1):
        f[i] = f[i - 1] + f[i]

    for i in range(n, 0, -1):
        j = (lista[i - 1] // 10 ** c) % 10
        y[f[j]] = lista[i - 1]
        f[j] -= 1

    for i in range(1, n + 1):
        lista[i - 1] = y[i]

    return lista


def putere(a, b):
    return a ** b