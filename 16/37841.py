count = 0
k = int(input())
for i in range(k):
    numbers = int(input())
    if numbers % 10 == 3:
        count += numbers

print(count)
