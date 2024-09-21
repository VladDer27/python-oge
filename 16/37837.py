numbers_sum = 0
t = int(input())
for i in range(t):
    number = int(input())
    if number % 10 == 4:
        numbers_sum += number
print(numbers_sum)
