diction = [(1, 2), (11, 2), (1, 12), (11, 12), (-11, -12), (-11, 12), (-12, 11), (10, 10), (10, 5)]
counter = 0
A_counter = 0
for A in range(-50, 51):
    for s, t in diction:
        if (s > 10) or (t > A):
            print("YES")
            counter += 1
        else:
            print("NO")
    if counter == 7:
        A_counter += 1
    counter = 0
print(A_counter)