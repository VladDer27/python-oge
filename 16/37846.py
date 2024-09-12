number_sum = 0
number = int(input())
while number != 0:
    if number % 6 == 0 and number % 10 == 4:
        number_sum += number

    number = int(input())

print(number_sum)
