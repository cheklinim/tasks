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


def is_palindrome(string):
    for i in range(len(string) // 2):
        if string[i] != string[-1 - i]:
            return False
    return True


def is_degenerated(x):
    """
    Функция возвращает истину, если отрезок вырожден в точку.
    На вход подаются координаты двух точек - кортежи a = (x1, y1), b = (x2, y2)
    """
    if x[0][0] == x[1][0] and x[0][1] == x[1][1]:
        return True
    return False


def is_vertical(x):
    """
    Функция возвращает истину, если отрезок вертикальный
    """
    if x[0][0] == x[1][0] and x[0][1] != x[1][1]:
        return True
    return False


def is_horizontal(x):
    """
    Функция возвращает истину, если отрезок горизонтальный
    """
    if x[0][1] == x[1][1] and x[0][0] != x[1][0]:
        return True
    return False


def is_inclined(x):
    """
    Функция возвращает истину, если отрезок наклонный
    """
    if x[0][0] != x[1][0] and x[0][1] != x[1][1]:
        return True
    return False


if __name__ == "__main__":
    """
    Модуль содержит функции-решения задач на Hexlet.io по специализации Python-программист.
    """
    print("Этот модуль нужно импортировать")

