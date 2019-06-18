'''
풀이:
    Brute Force로 품.
    남은 작업량 = 100 - progress
    배포일 = 남은 작업량 / 속도
    로 배포일 계산 후 배포되는 갯수 계산
 2019.06.19 - 정답
    n = 0 < progresses < 100
    m = 0 <= speed <= 100
    시간복잡도:O(n)
    공간복잡도:O(n+m)
'''

import math

def solution(progresses, speeds):
    answer = []
    cnt = 0 # 배포 갯수
    deploy_day = 0 # 리스트에서 이전 기능의 배포일
    for idx, progress in enumerate(progresses, 0):
        remain_progress = 100 - progress # 남은 작업량 계산
        if idx == 0:
            # 최초 기능 배포일 계산
            deploy_day = math.ceil(remain_progress / speeds[idx])
            cnt += 1
        else:
            if deploy_day >= math.ceil(remain_progress / speeds[idx]):
                # 앞선 기능과 함께 배포되는 기능 갯수 계산
                cnt +=1
            else:
                # 추 후 배포되는 기능
                answer.append(cnt)
                deploy_day = math.ceil(remain_progress / speeds[idx])
                cnt = 1

    answer.append(cnt)
    return answer
