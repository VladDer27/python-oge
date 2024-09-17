min = 30001
s = int(input())
for i in range(s):
    numbers = int(input())
    if numbers % 10 == 4 and numbers < min:
        min = numbers

print(min)
