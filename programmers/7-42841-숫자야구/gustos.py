'''
풀이:
 2019.07.01 - 정답:
    정환이랑 똑같이 품
'''

import itertools
def solution(baseball):
    answer = 0
    pool = [str(i) for i in range(1, 10)]
    tmp_list = list(map(''.join, itertools.permutations(pool, 3)))
    for t in tmp_list:
        flag = True
        for b in baseball:
            if not is_correct(b, t):
                flag = False
                break

        if flag:
            answer += 1
    return answer

def is_correct(baseball, num2):
    num1 = str(baseball[0])
    num2 = str(num2)
    s = 0
    b = 0
    for idx in range(0, 3):
        if num1[idx] == num2[idx]:
            s += 1
        elif num2[idx] in num1:
            b += 1
    if (baseball[1], baseball[2]) == (s, b):
        return True
    else:
        return False
