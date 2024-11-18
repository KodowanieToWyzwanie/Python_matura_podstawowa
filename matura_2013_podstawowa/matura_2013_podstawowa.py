with open("napisy.txt", "r") as file:
    dane = file.read().split()

len_even = 0
for napis in dane:
    if len(napis) % 2 == 0:
        len_even += 1
with open("zadanie4.txt", "a") as file:
    file.write(f"napisy o parzystej dlugosci {len_even}\n")

count_equal = 0
for napis in dane:
    if napis.count("1") == napis.count("0"):
        count_equal += 1
with open("zadanie4.txt", "a") as file:
    file.write(f"tyle samo 0 i 1 - {count_equal}\n")
only_ones = 0
only_zero = 0
for napis in dane:
    if napis.count("1") == len(napis):
        only_ones += 1
    if napis.count("0") == len(napis):
        only_zero += 1
with open("zadanie4.txt", "a") as file:
    file.write(f"same 1 - {only_ones} same 0 - {only_zero}\n")

tab_result = [0]*17
for napis in dane:
    tab_result[len(napis)] += 1
with open("zadanie4.txt", "a") as file:
    for key, value in enumerate(tab_result):
        if key > 1:

            file.write(f"{key} znakow  {value}\n")

