# 가격 개수 입력 조건
#   2 <= n <= 2 * 10의 5승
priceCnt = int(input("집 가격 개수를 입력해주세요: "))
if priceCnt < 2 or priceCnt > (2 * pow(10, 5)):
    print("집 가격 개수 조건을 확인해주세요!!")
    exit()

# 가격 범위 입력 조건
#   모든 가격은 중복되지 않는다.
#   1 <= price[i] <= 10의 16승
priceList = list(map(int, input("집 가격 개수만큼의 가격을 입력해주세요: ").split()))
if len(priceList) != len(set(priceList)):
    print("집 가격 조건을 확인해주세요!!(중복)")
    exit()

for a in priceList:
    if a < 1 or a > pow(10, 16):
        print("집 가격 조건을 확인해주세요!!(가격범위)")
        exit()

# 반복문을 통해서 처음부터 최적의 값을 찾아내고, 가장 적은 손실을 보는 가격을 출력한다
pnt = 0
ret = 0

for i in priceList:
    for y in priceList[pnt:]:
        if (i - y) > 0:
            if ret > (i - y) or ret == 0:
                ret = (i - y)
    pnt = pnt + 1

print(ret)
