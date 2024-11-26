num = 0
sr = 0
n = int(input())
for i in range(1, n + 1):
    a = int(input())
    sr += a
    if a > 0: num += 1
sr = sr / n
print(sr)
if num >= 5: print('YES')
else: print('NO')