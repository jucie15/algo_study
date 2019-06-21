'''
풀이:
    BruteForce??
    DFS로 모든 경우의 수 체크하여 정답 도출출

 2019.06.21 - 정답
    n = 2 <= numbers < 20
    m = 1 <= target <= 1000
    시간복잡도:O(2^n)
    공간복잡도:O(n+m)
'''

def solution(numbers, target):
    answer = f_calc(numbers, target, 0, 0, 0)
    answer += f_calc(numbers, target, 0, 0, 1)

    return answer


def f_calc(numbers, target, calc, idx, operator):
    if operator == 0:
        calc = calc - numbers[idx]
    else:
        calc = calc + numbers[idx]

    if(idx == len(numbers) - 1):
        if target == calc:
            return 1
        else:
            return 0
    else:
        return f_calc(numbers, target, calc, idx + 1, 0) + f_calc(numbers, target, calc, idx + 1, 1)
