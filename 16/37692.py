n = int(input())
s = 0
a = 0
for i in range(n):
    x = int(input())
    if x > 0:
        s += x
        a += 1
print(s / a)
print(a)
