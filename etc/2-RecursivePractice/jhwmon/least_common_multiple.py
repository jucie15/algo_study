import numpy

# numA와 numB를 인수분해해서 인수들을 list에 저장
def factorization(numA, numB, list) :
    if (numA % 2) == 0 and (numB % 2) == 0:
        list.append(2)
        numA /= 2
        numB /= 2
    elif (numA % 3) == 0 and (numB % 3) == 0:
        list.append(3)
        numA /= 3
        numB /= 3
    else:
        list.append(int(numA))
        list.append(int(numB))
        numA = 0
        numB = 0

    if numA != 0 or numB != 0:
        factorization(numA, numB, list)

# numberA와 numberB의 최소 공배수 구하기
numberA = int(input())
numberB = int(input())
leastMultiple = []

# 0을 입력받을 경우 종료
if numberA == 0 or numberB == 0:
    print("0은 공배수를 구할 수 없습니다")
    exit()

# 재귀함수를 이용해서 인수분해
factorization(numberA, numberB, leastMultiple)

print(numpy.prod(leastMultiple))