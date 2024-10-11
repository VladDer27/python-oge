max1 = -30001
max2 = -30001
min1 = 30001
min2 = 30001
numbers = int(input())
while numbers != 0:
    if numbers > max1:
        max2 = max1
        max1 = numbers
    elif numbers > max2:
        max2 = numbers

    if numbers < min1:
        min2 = min1
        min1 = numbers
    elif numbers < min2:
        min2 = numbers

    numbers = int(input())

print(max1 + max2)
print(min1 + min2)