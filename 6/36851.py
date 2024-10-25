def fs(s, t, A):
    if (s > A) or (t > 12):
        return 1
    else:
        return 0


a = ((13, 2), (11, 12), (-12, 12), (2, -2), (-10, -10), (6, -5), (2, 8), (9, 10), (1, 13))
kol = 0
for A in range(100):
    count = 0
    for i in range(9):
        count += fs(a[i][0], a[i][1], A)
    if count == 4:
        print(A)
        break
