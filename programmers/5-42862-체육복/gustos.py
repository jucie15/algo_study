
def solution(n, lost, reserve):
    answer = 0
    len_lost = len(lost)
    for idx in range(len(lost)):
        if lost[idx] in reserve:
            reserve.remove(lost[idx])
            lost[idx] = -9999
            answer += 1

    for r in reserve:
        for l in lost:
            if l - 1 == r or l + 1 == r:
                lost.remove(l)
                answer += 1
                break

    return n - len_lost + answer
