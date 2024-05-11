import random

total_numbers = 100


files = ['100_numere_random.txt', "1000_numere_random.txt", "10000_numere_random.txt", "100000_numere_random.txt"]

for file in files:
    with open(file, 'w') as f:
        for _ in range(total_numbers):
            x = random.randint(0, 1000)
            f.write(str(x) + ' ')
        total_numbers = total_numbers * 10;

files2 = ['100_numere_sorted.txt', '1000_numere_sorted.txt', '10000_numere_sorted.txt', '100000_numere_sorted.txt']

total_numbers = 100

for file in files2:
    with open(file, 'w') as f:
        for i in range(total_numbers+1):
            f.write(str(i) + ' ')
        total_numbers = total_numbers * 10;


files3 = ['100_numere_reversesorted.txt', '1000_numere_reversesorted.txt', '10000_numere_reversesorted.txt', '100000_numere_reversesorted.txt']

total_numbers = 100

for file in files3:
    with open(file, 'w') as f:
        for i in range(total_numbers,-1,-1):
            f.write(str(i) + ' ')
        total_numbers = total_numbers * 10;