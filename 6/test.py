number = 10

arr = []

for i in range(5):
    arr.append(i)

arr.reverse()
arr.pop()
arr.remove(4)
print(arr)


def f(x):
    return x ** 2 + 2 * x - 4


def loop(x, y):
    for i in range(y):
        x += 3
    return x


print(f(3))
number = loop(number, 5)
number = loop(number, 6)
print(number)
