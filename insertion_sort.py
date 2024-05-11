def insertion_sort(lista):
    for i in range(1, len(lista)):
        val = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > val:
            lista[j + 1] = lista[j]
            j = j - 1
        lista[j + 1] = val

    return lista