summ = 0
a = 0
f = 0
number = int(input())
while number != 0:
    summ += number
    if number < 0:
        f += 1
    else:
        number += 1
    number = int(input())
print(summ)
print(number - f)