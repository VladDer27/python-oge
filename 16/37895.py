n = int(input())
maxi = -1
for i in range(1, n + 1):
    a = int(input())
    if a % 5 == 0 and a > maxi:
        maxi = a
print(maxi)