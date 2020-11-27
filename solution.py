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


if __name__ == "__main__":
    """
    Модуль содержит функции-решения задач на Hexlet.io по специализации Python-программист.
    """
    print("Этот модуль нужно импортировать")
