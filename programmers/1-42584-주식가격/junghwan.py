'''
19. 06. 14

오답: 실행 시 문제에 있는 테스트 케이스 [1,2,3,2,3]은 정답, 채점 시
테스트케이스 1번을 제외하고 다 틀림(효율성 마저도)

구현 방식에서의 문제점: 비효율적인 이중 for문 사용(O(n^2) 시간 복잡도 예상),
(바로 다음 원소가 감소하더라도 기본적으로 1초가 걸리는 부분에 대한 예외처리 부족 예상)

-----

정답: 반복문을 돌리면서 불필요한(중복되는)연산 제거,
기본적으로 1초가 걸리는 부분에 대해서 결과 리스트에 추가할 때 1을 더해줌,
마지막 원소는 항상 0초 이기에 반복문에서 제외, return 하기 전에 별도로 추

'''


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
