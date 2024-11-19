def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def sum_digit(a):
    suma = 0
    while a > 0:
        suma = suma + a % 10
        a //= 10
    return suma


with open("PARY_LICZB.TXT", "r") as file:
    dane = [i.split() for i in file]

print(dane)

count_multiple = 0
wzglednie_pierwsze = 0
sum_digt_same = 0
for i in dane:
    a, b = int(i[0]), int(i[1])
    if a % b == 0 or b % a == 0:
        count_multiple += 1
    if nwd(a, b) == 1:
        wzglednie_pierwsze += 1
    if sum_digit(a) == sum_digit(b):
        sum_digt_same += 1

with open("zadanie5.txt", "w") as file:
    file.write(f"a) {count_multiple}\n")
    file.write(f"b) {wzglednie_pierwsze}\n")
    file.write(f"c) {sum_digt_same}\n")
