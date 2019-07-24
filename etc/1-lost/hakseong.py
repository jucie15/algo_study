# -*- coding: utf-8 -*-

"""
장훈이에게는 특정 집의 햔후 몇 년간 금액을 예상한 차트가 있다. 장훈이는 특정 해에 집을 구입한 후 다른해에 꼭 손실을 보면서 팔아야 한다. 장훈이는 이 와중에 자산손실을 최소화 하고 싶다.
n = 5년치의 집의 가치가 price= [20, 15, 8, 2, 12]이라고 하자. 장훈이는 어느 해에든 집을 구입할 수 있지만, 그 후 한번은 손실을 보며 집을 되팔아야 한다. 위 상황이라면 2년째인 price[1] = 15에 구매하고, 5년 째인 price[4] = 12에 되팔 때 손실을 최소화 할 수 있을까?

"""


def minLossForResell(price):


    ## 파이썬의 성능 최적화에 대해 알아봐야함
    ## 나중에 질문사항으로 어떻게 최적화를 하는지 여쭈어 보자

    ex = 9999
    pre = 0
    post = 0
    print("len의 값은 : " + str(len(price)))
    ## x는 구할때의 금액을 지정, y는 판매할 때의 가격을 지정
    for x in range(0,len(price)):
#        print("x의 값은 : " + str(x))
        for y in range(0,len(price)):
#            print("ex의 값은 : " + str(abs(ex)))
#            print("[x]의 값은 : " + str(x))
#            print("[y]의 값은 : " + str(y))
#            print("price[x]-price[y]의 값은 : " + str(price[x]-price[y]))
#            print(ex >price[x]-price[y])
#            print(x < y)
#            print(0 < price[x]-price[y])
            if ex > price[x]-price[y] and x < y and 0 < price[x]-price[y]: ## 계속되는 입력금액이 x-y 보다 커야하고, 그리고 x 시작점은 y보다 작아야함 (크거나 같으면 불필요한 움직임 발생)
                ex = price[x]-price[y] ## 구입 - 판매 금액
                pre = x ## 구입 년
                post = y ## 판매 년
                print("[pre]의 값은 : " + str(pre))
                print("[post]의 값은 : " + str(post))



    return ex




n = 5

## 실 문제
#price = [20, 15, 8, 2, 12]
## 예비문제 - 답이 2가 나와야함
price = [20, 7, 8, 2, 5]
print(minLossForResell(price))
#ex = 0
#pre = 0
#post = 0
### x는 구할때의 금액을 지정, y는 판매할 때의 가격을 지정
#for x in range(0,len(price)):
#    for y in range(0,len(price)):
#        if ex > price[x]-price[y] and x < y: ## 계속되는 입력금액이 x-y 보다 커야하고, 그리고 x 시작점은 y보다 작아야함 (크거나 같으면 불필요한 움직임 발생)
#            ex = abs(price[x]-price[y])
#            pre = x + 1
#            post = y + 1
#
#
#print (ex)
#print (pre)
