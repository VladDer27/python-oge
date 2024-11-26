count = 0
a = 1
while a != 0:
    a = int(input())
    if a == 0:
        break
    if a % 3 == 0 and a // 10 == 0:
        count += 1
print(count)