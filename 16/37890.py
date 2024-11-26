count = 0
a = 1
while a != 0:
    a = int(input())
    if a == 0:
        break
    if a % 5 == 0 or a % 9 == 0:
        count += 1
print(count)