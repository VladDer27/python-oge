count = 0
top = 0
n = int(input())
for i in range(1, n + 1):
    a = int(input())
    if a < 5:
        count += 1
    if a == 10:
        top = 1
print(count)
if top == 1:
    print('YES')
else:
    print('NO')