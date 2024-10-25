def fs(s, k):
    if s >= 2 * k:
        return 1
    else:
        return 0


a = ((1, 2), (8, 4), (6, -12), (-5, -5), (3, 11), (-10, 12), (-10, -2), (4, 1), (2, 5))
kol = 0
for i in range(9):
    kol += fs(a[i][0], a[i][1])
print(kol)
