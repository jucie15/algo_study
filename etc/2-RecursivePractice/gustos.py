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

if __name__ == "__main__":
    n = int(input("숫자를 입력해주세요: "))
    # print(factorial(n))
    divide_digit(n)
    print(fibonacci(n))
