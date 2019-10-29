# 정답
def solution(clothes):
    temp = dict()
    for cloth in clothes:
        if cloth[1] in temp:
            temp[cloth[1]] +=1
        else:
            temp[cloth[1]] = 1
    answer = 1
    for k, v in temp.items():
        answer *= (v + 1)

    answer -= 1

    return answer
