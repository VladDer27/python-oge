max = 0
h = int(input())
for i in range(h):
    numbers = int(input())
    if numbers % 10 == 3 and numbers > max:
        max = numbers

print(max)
