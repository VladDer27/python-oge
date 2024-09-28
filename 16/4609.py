counter = 0
number = int(input())
while number != 0:
    if number % 5 == 0 or number % 9 == 0:
        counter += 1
    number = int(input())
print(counter)
