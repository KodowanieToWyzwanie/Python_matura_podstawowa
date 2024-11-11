def digit_sum(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number //= 10
    return  sum

with open("cyfry.txt", "r") as file:
    dane = file.read().split()

count_even = 0
max_digit_sum = 0
digit_max = 0
min_dgit_sum = 99999999999999999999999999999999999999999999999999999
digit_min = 0
for liczba in dane:
    liczba = int(liczba)
    if liczba % 2 == 0:
        count_even += 1
    sum_digit_number = digit_sum(liczba)
    if sum_digit_number > max_digit_sum:
        max_digit_sum = sum_digit_number
        digit_max = liczba
    if sum_digit_number < min_dgit_sum:
        min_dgit_sum = sum_digit_number
        digit_min = liczba

tab_ros = []
for number in dane:
    for i in range(len(number)-1):
        if number[i] >= number[i +1]:
            break
    else:
        tab_ros.append(number)


with open("zadanie4.txt", "w+") as file:
        file.write(f"w pliku jest {count_even} liczb parzystych\n")

        file.write(f"liczba o najwiekszej sumie cyfr rownej {max_digit_sum} to {digit_max}\n")
        file.write(f"liczba o najmniejszej sumie cyfr rownej {min_dgit_sum} to {digit_min}\n")
        for i in tab_ros:
            file.write(f"{i} ")

