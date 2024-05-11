def selectionsort(lista):
    for i in range(0, len(lista)):
        k = i
        for j in range(i + 1, len(lista)):
            if lista[k] > lista[j]:
                k = j
        if k != i:
            lista[i], lista[k] = lista[k], lista[i]

    return lista