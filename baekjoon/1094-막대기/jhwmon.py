# -*- coding: utf-8 -*-
# x 는 64를 초과하지 않는다
x = int(input())
if x > 64:
    print("x 값이 64cm를 초과했습니다.")
    exit()
# 2의 제곱 중 가장 큰 수를 차례로 x에서 뺀다
stick = 0

# x가 0이 되면 완료
while x > 0:
    flag = 0
    i = 0

    while flag < 1:
        sum = 2 ** i

        if sum > x:
            x -= 2 ** (i-1)
            stick += 1
            flag += 1
        elif sum == x:
            x -= 2 ** i
            stick += 1
            flag += 1

        i += 1

# x에서 몇번을 뺐는지 출력한다.
print(stick)