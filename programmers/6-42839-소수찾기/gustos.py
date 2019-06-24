'''
풀이:
    선행 스킬 순서(인덱스를 이용)대로 스킬트리에 있는 순서 체크
 2019.06.24 - 정답:
    재귀로 모든 경우의 수 탐색 answer_list, 와 idx_list를 추가하여 불필요한 경우까지 모두 탐색하는 경우가 있는 것 같음 재귀 점화식을 다시 생각해볼 필요가 있음
    시간과 공간복잡도 모두 최악인 듯
    중복되는 경우까지 모두 계산 후 answer_list에 담은 후 마지막에 중복 제거 후 갯수 계산

    n = 1 <= numbers <= 7
    시간복잡도: O(4^n-1)
    공간복잡도: O(n)
'''

def solution(numbers):
    answer = 0
    answer_list = []
    for idx, number in enumerate(numbers, 0):
        if int(number) != 0:
            answer_list += find_prime(numbers, number, [idx], [])

    answer = len(set(answer_list))
    return answer


def is_prime(number):
    number = int(number)
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0 or number == 1 or number == 0:
            return False

    return True


def find_prime(numbers, calc, idx_list, answer_list):
    if is_prime(calc):
        answer_list.append(calc)

    if len(numbers) == len(idx_list):
        return answer_list

    for idx, number in enumerate(numbers, 0):
        if idx not in idx_list:
            idx_list.append(idx)
            answer_list = find_prime(numbers, calc + number, idx_list, answer_list)
            idx_list.remove(idx)

    return answer_list
