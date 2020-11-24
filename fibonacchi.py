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


def main():
    print("Искомое число Фибоначчи:", fib(int(input("Введите искомое число Фибоначчи: "))))


if __name__ == "__main__":
    main()
