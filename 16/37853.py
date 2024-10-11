n = 0
number = 0
a = int(input())
while a != 0:
    number += 1
    if (a % 2 != 0) and (a % 3 == 0):
        n += 1
    a = int(input())
print(number)
print(n)
