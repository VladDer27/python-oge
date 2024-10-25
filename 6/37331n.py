def fs(s, t, A):
    if (s > 10) or (t > A):
        return 1
    else:
        return 0
a = ((1, 2), (11, 2), (1, 12), (11, 12), (-11, -12), (-11, 12), (-12, 11), (10, 10), (10, 5))
kol = 0
for A in range(100):
    count = 0
    for i in range(9):
        count += fs(a[i][0], a[i][1], A)
    if count == 7:
        kol += 1
print(kol)