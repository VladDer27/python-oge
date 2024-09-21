count = 0
s = int(input())
for i in range(s):
    numbers = int(input())
    if numbers % 10 == 6:
        count += 1

print(count)
