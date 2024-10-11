summ = 0
l = 0
number = int(input())
while number != 0:
    l += 1
    if (number % 2 == 0) and (number > 0) and (number <= 256):
        summ += number
    number = int(input())
print(l)
print(summ)
