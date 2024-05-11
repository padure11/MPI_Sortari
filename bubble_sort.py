def bubblesort(lista):
    n = len(lista)
    for i in range(n-1):
        for j in range(i+1, n):
            if lista[j] < lista[i]:
                lista[j], lista[i] = lista[i], lista[j]

    return lista