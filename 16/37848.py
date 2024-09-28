max = 0
g = True
s = int(input())
for i in range(s):
    numbers = int(input())
    if numbers > max:
        max = numbers
    if g and numbers < 30:
        g = False

print(max)
if g:
    print("NO")
else:
    print("YES")
