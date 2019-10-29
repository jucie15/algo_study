# 정답
def solution(participant, completion):
    p = dict()
    for name in participant:
        if name in p:
            p[name] += 1
        else:
            p[name] = 1
    for name in completion:
        p[name] -= 1
        if p[name] < 1:
            del(p[name])

    answer = list(p.keys())[0]
    return answer
