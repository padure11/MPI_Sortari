def quicksort(lista):
    if len(lista) <= 1:
        return lista

    pivot = lista[len(lista) // 2]

    stanga = []
    dreapta = []
    mijloc = []

    for i in lista:
        if i < pivot:
            stanga.append(i)
        if i > pivot:
            dreapta.append(i)
        if i == pivot:
            mijloc.append(i)

    return quicksort(stanga) + mijloc + quicksort(dreapta)