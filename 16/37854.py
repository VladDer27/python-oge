summ = 0
a = 0
number = int(input())
while number != 0:
    summ += number
    if (number % 2 == 0) and (number % 5 == 0):
        a += 1
    number = int(input())
print(summ)
print(a)