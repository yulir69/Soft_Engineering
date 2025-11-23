def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


if __name__ == '__main__':

    with open('fib.txt', 'w') as f:
        for num in fib(200):
            f.write(str(num) + '\n')

    print("Числа Фибоначчи записаны в файл fib.txt")