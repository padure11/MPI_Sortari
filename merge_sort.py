def mergesort(lista):
    if len(lista) <= 1:
        return lista

    mijloc = int(len(lista) // 2)
    lista_stanga = (mergesort(lista[:mijloc]))
    lista_dreapta = (mergesort(lista[mijloc:]))
    return interclasare(lista_stanga, lista_dreapta)


def interclasare(lista_stanga, lista_dreapta):
    i = 0
    j = 0

    mergelist = []

    while i < len(lista_stanga) and j < len(lista_dreapta):
        if lista_stanga[i] < lista_dreapta[j]:
            mergelist.append(lista_stanga[i])
            i = i + 1

        else:
            mergelist.append(lista_dreapta[j])
            j = j + 1

    mergelist = mergelist + lista_stanga[i:]
    mergelist = mergelist + lista_dreapta[j:]

    return mergelist