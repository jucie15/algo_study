def fibonacci(num):
    # 입력받은 값이 2 이상이면 ??
    if num > 3:
        return fibonacci(num - 1) + fibonacci(num - 2)
        # result = fibonacci(num - 1) + fibonacci(num - 2)
    elif num == 3:
        return 1
    elif num == 2:
        return 1
    elif num == 1:
        return 0
    else :
        print("파라미터 입력 에러")
        exit()

# 피보나치 수를 구해라
# ex) 0 1 1 2 3 5 8 13 21 34 55 89 144 233...
number = int(input())

print(fibonacci(number))

