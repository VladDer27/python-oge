summ = 0
numbers = int(input())
while numbers != 0:
    if numbers % 7 == 0 and numbers % 10 == 3:
        summ = numbers + summ

    numbers = int(input())

print(summ)
