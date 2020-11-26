def binary_sum(a, b):
    a = int(a, 2)
    b = int(b, 2)
    return bin(a + b)[2:]


def main():
    a, b = input("Введите два двоичных числа, разделенных пробелом: ").split()
    print(binary_sum(a, b))


if __name__ == "__main__":
    """
    Модуль содержит функцию binary_sum(), которая возвращает сумму двоичных числе в виде строки
    """
    main()
