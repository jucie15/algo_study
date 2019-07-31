# -*- coding: utf-8 -*-
# 단어 입력받는다 (1,000,000 넘지않는 단어)
verb = input()

 # 알파벳:카운트의 해쉬를 생성해서 각자 카운트한다.
alphabet = dict()
for i in range(97, 123):
    alphabet[chr(i)] = 0

for i in list(verb.lower()):
    alphabet[i] += 1

ret = 0
col = 0
for y in alphabet:
    if ret < alphabet[y]:
        ret = alphabet[y]
        col = y.upper()
    elif ret == alphabet[y]:
        col = '?'

print(col)
