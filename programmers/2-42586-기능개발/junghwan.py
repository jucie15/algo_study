# 기능개발

'''
19. 06. 20

풀이: day list 안에 배포까지 남은 일자 계산 후 append
반복문을 통해 대소 비교 후 cnt 값 증가 및 answer 리스트에 append

기존 js로 풀었던 방식으로 해결해보려 했으나, 비효율적이고 문법적으로도 이슈가 있었음
(인덱스 값을 다른 변수에 저장할 때 발생)

'''

import math

def solution(progresses, speeds):
    answer = []
    day = []

    for i in range(len(progresses)):
        day.append(math.ceil((100 - progresses[i]) / speeds[i]))

    idx = 0
    cnt = 1
    i = 1
    while i < len(day):

        if day[idx] < day[i]:
            idx = i
            answer.append(cnt)
            cnt = 0
        
        else:
            i = i + 1
            cnt = cnt + 1

    answer.append(cnt)
    print(answer)

    return answer