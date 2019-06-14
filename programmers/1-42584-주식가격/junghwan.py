def solution(prices):
    answer = []
    sec = 0
    start = 0
    d = prices
    length = len(prices)

    while length > start+1 :
        sec = 0

        for i in range(start+1, length-1):
            if(d[start] > d[i] ) :
                break
            else:
                sec = sec + 1

        start = start + 1
        answer.append(sec+1)

    answer.append(0)

    return answer
