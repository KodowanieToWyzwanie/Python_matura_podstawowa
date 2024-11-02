import math
with open ('matura_2009_podstawowa_plik.txt', 'r') as f:
    dane = list(map(int, f.read().split()))

def is_prime(number):
    if number < 2:
        return False
    else:
        return all(number % i != 0 for i in range(2, int(number/2 + 1)))



with open("zad_5.txt", "a+") as file:
    for number in dane:
        a = int(math.sqrt(number))
        for i in range(a - 1, a + 1):
            if i * i == number and is_prime(i):
                file.write(str(number)+"\n")
