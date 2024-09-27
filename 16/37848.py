max = 0
g = "No"
s = int(input())
for i in range(s):
    numbers = int(input())
    if numbers > max:
        max = numbers
    if numbers < 30:
        g = "Yes"

print(max, g)
