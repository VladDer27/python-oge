def fs(s, t):
    if s > 10 or t > 10:
        return 1
    else:
        return 0


counter = 0
runs = ((1, 2), (11, 2), (1, 12), (11, 12), (-11, -12), (-11, 12), (-12, 11), (10, 10), (10, 5))
for i in range(len(runs)):
    if fs(runs[i][0], runs[i][1]) == 1:
        counter += 1
print(counter)
