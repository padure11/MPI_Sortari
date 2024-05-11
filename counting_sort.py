def countingsort(lista, m):
    f = [0] * m
    result = [0] * len(lista)

    for i in range(len(lista)):
        f[lista[i]] += 1

    for i in range(1, m):
        f[i] = f[i - 1] + f[i]

    for i in reversed(range(len(lista))):
        result[f[lista[i]] - 1] = lista[i]
        f[lista[i]] = f[lista[i]] - 1

    for i in range(len(lista)):
        lista[i] = result[i]

    return result