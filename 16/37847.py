max1 = -30001
max2 = -30001
min1 = 30001
min2 = 30001
number = int(input())
while number != 0:
    if number > max1:
        max2 = max1
        max1 = number
    elif number > max2:
        max2 = number

    if number < min1:
        min2 = min1
        min1 = number
    elif number < min2:
        min2 = number

    number = int(input())

print(max1 + max2)
print(min1 + min2)
