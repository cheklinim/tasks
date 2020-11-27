def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    f1, f2 = 0, 1
    m = 2
    while m <= n:
        f1, f2 = f2, f1 + f2
        m += 1
    return f2


def binary_sum(a, b):
    a = int(a, 2)
    b = int(b, 2)
    return bin(a + b)[2:]


def fizz_buzz(begin, end):
    result = []
    for i in range(begin, end + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append('FizzBuzz')
        elif i % 3 == 0:
            result.append('Fizz')
        elif i % 5 == 0:
            result.append('Buzz')
        else:
            result.append(str(i))
    return ' '.join(result)


if __name__ == "__main__":
    """
    Модуль содержит функции-решения задач на Hexlet.io по специализации Python-программист.
    """
    print("Этот модуль нужно импортировать")

