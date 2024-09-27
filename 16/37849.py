min = 301
a = "No"
s = int(input())
for i in range(s):
    numbers = int(input())
    if numbers < min:
        min = numbers
    if numbers < 80:
        a = "Yes"

print(min, a)
