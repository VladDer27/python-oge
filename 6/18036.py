def fs(s, t, A):
    if (s > A) or (t > 12):
        return 1
    else:
        return 0


runs = ((13, 2), (11, 12), (-12, 12), (2, -2), (-10, -10), (6, -5), (2, 8), (9, 10), (1, 13))

for A in range(-100, 101):
    counter = 0
    for i in range(len(runs)):
        if fs(runs[i][0], runs[i][1], A) == 0:
            counter += 1
    if counter == 8:
        print(A)
        break

