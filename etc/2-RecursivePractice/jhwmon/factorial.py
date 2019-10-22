def factorial(num) :
    total = num

    if num > 1:
        total *= factorial(num - 1)

    return total

number = int(input())

# result = 1
# for i in range(number, 0, -1):
#     result *= i
#
# print(result)

print(factorial(number))