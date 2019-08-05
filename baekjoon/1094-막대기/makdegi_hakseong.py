# -*- coding: utf-8 -*-


## input이 있으니 python으로 실행 후 내용을 입력해야함
ex = int(input())
a = 64
count = 0
while True:
    if a <= ex:
        count = count + 1
        ex = ex - a
    if a == 1:
        break
    a = a / 2


print(count)
