'''
19. 06. 22

DFS 개념 활용
덧셈과 뺄셈을 했을 경우를 더하면서 결과 도출

'''

def solution(numbers, target):
    answer = calc(numbers, target, 0, 0)
    return answer


def calc(numbers, target, _sum, idx):
    
    if idx == len(numbers):
        if _sum == target:
            return 1
        else:
            return 0
    
    return calc(numbers, target, _sum+numbers[idx], idx+1) + calc(numbers, target, _sum-numbers[idx], idx+1)