N = int(input())
tc = 0
s = 0
for i in range(N):
    number = int(input())
    if number > 0:
        tc += 1
        s += number
print(s / tc)
print(tc)
