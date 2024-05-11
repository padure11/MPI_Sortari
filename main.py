import time
import sys
import bubble_sort
import merge_sort
import selection_sort
import insertion_sort
import quick_sort

sys.setrecursionlimit(10000000)


for _ in range(5):

    lista_bubble_sort = []
    lista_insertion_sort = []
    lista_selection_sort = []
    lista_quick_sort = []
    lista_merge_sort = []



    with open('input_file', 'r') as file: #input_file = fisierul de input

        numbers = []
        content = file.read()
        numbers_str = content.split()
        for num_str in numbers_str:
            lista_bubble_sort.append(int(num_str))
            lista_selection_sort.append(int(num_str))
            lista_quick_sort.append(int(num_str))
            lista_merge_sort.append(int(num_str))
            lista_insertion_sort.append(int(num_str))

    timpi = []

    start_time = time.time()
    lista1_sort = bubble_sort.bubblesort(lista_bubble_sort)
    timpi.append(time.time() - start_time)

    start_time = time.time()
    lista2_sort = insertion_sort.insertion_sort(lista_insertion_sort)
    timpi.append(time.time() - start_time)

    start_time = time.time()
    lista3_sort = selection_sort.selectionsort(lista_selection_sort)
    timpi.append(time.time() - start_time)

    start_time = time.time()
    lista4_sort = quick_sort.quicksort(lista_quick_sort)
    timpi.append(time.time() - start_time)

    start_time = time.time()
    lista5_sort = merge_sort.mergesort(lista_quick_sort)
    timpi.append(time.time() - start_time)
