count = 0
l = "No"
s = int(input())
for i in range(s):
    numbers = int(input())
    count += numbers

    if numbers < 40:
        l = "Yes"

print(count, l)
