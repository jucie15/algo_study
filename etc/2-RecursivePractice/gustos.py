import time
import sys
sys.setrecursionlimit(1000000)

def factorial(n):
    if n == 1:
        return 1
    else:
        return n + factorial(n-1)


def divide_digit(n):
    if n < 10:
        print(int(n))
    else:
        divide_digit(n / 10)
        print(int(n % 10))


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


memoize = [int(-1) for i in range(1000)]

def dp_fibonacci(n):
    if memoize[n] != -1:
        return memoize[n]

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        memoize[n] = dp_fibonacci(n - 1) + dp_fibonacci(n - 2)
        return memoize[n]


if __name__ == "__main__":
    n = int(input("숫자를 입력해주세요: "))
    # print(factorial(n))
    divide_digit(n)
    start = time.time()
    print(fibonacci(n))
    print('피보1: ', time.time() - start)
    start = time.time()
    print(dp_fibonacci(n))
    print('피보2: ', time.time() - start)

