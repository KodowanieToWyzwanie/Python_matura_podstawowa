with open("../../../Downloads/matura_2011_podstawowa/hasla.txt", "r") as file:
    data = file.read().split()

# W pliku wynik4a.txt podaj, ile haseł ma parzystą, a ile nieparzystą liczbę znaków.
even = 0
odd = 0

for item in data:
    if len(item) % 2 == 0:
        even += 1
    else:
        odd += 1
with open("wynik4a.txt", "a+") as file:
    file.write(f"{even} hasel ma parzysta liczbe znakow, a {odd}  nieparzysta")


# W pliku wynik4b.txt utwórz zestawienie haseł (po jednym w wierszu), które są
# palindromami.
# Palindrom to wyraz brzmiący tak samo przy czytaniu z lewej strony do prawej, jak
# i odwrotnie, np. kajak, potop.
with open("wynik4b.txt", "a+") as file:
    for i in data:
        if i == i[::-1]:
            file.write(f"{i} \n")

# Zapisz w pliku wynik4c.txt zestawienie haseł (po jednym w wierszu) zawierających
# w sobie dwa kolejne znaki, których suma kodów ASCII wynosi 220.
def suma220(item):
    for i in range(len(item)-1):
        if ord(item[i]) + ord(item[i+1]) == 220:
            return True

with open("wynik4c.txt", "a+") as file:
    for item in data:
        if suma220(item):
            file.write(f"{item}\n")