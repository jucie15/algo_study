'''
풀이:
    answer = 가격이 떨어진 시점(price_index) - 가격 초기 생성 시점(price_index)를 뺀 수.
    가격이 떨어지기 전까지의 price들을 tmp_list에 추가한 후 떨어진 시점 발생 시 tmp_list에 있는 값들을 가져와 비교 후
    떨어진 값의 경우 answer 값을 계산하여 추가해준다.
 2019.06.14 - 오답(10%): answer 답 삽입 시 insert함수 사용으로 인한 Timeout Error
 2019.06.14 -
    정답: 찝찝하지만, answer를 price 크기만큼 초기 생성 후 해당 인덱스에 바로 답 삽입으로 코드 수정
    시간복잡도:O(n)
    공간복잡도:O(n)
    Todo: 공간 복잡도 최적화 및 가격이 떨어졌을 떄 tmp_list에 있는 값 순회 시 같은 값까지 비교하는 연산 줄이기
'''
def solution(prices):
    tmp_list = [] # 가격이 떨어지지 않은 주식 리스트
    answer = prices
    for idx in range(len(prices)-1):
        if prices[idx] <= prices[idx+1]:
            tmp_list.append(
                {
                    'idx': idx,
                    'price': prices[idx]
                })
        else:
            answer[idx] = 1
            while len(tmp_list) != 0:
                if tmp_list[-1]['price'] > prices[idx+1]:
                    tmp = tmp_list.pop()
                    answer[tmp['idx']] =  idx + 1 - tmp['idx']
                else:
                    break
    for tmp in tmp_list:
        answer[tmp['idx']] = len(prices) - tmp['idx'] - 1
    answer[-1] = 0
    return answer
