min = 30001
f = int(input())
for i in range (f):
    numbers = int(input())
    if numbers % 10 == 6 and numbers < min:
        min = numbers

print(min)