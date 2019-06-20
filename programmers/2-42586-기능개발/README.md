### 해설

배포까지 남은 일자를 '올림'을 이용해 계산하고, 리스트의 원소들 간 대소 비교를 통해

결과를 도출해내는 문제인 듯  하다.

n = 0 < progresses < 100

m = 0 <= speed <= 100

시간복잡도: `O(n)`

공간복잡도: `O(n+m)`



```python
import math

def solution(progresses, speeds):
    left_days = []
    now_left_day = 0
    # 처음 프로세스는 무조건 배포될것이기 때문에 1로 초기화
    deploy_count = 1
    answer = []

    # 각 프로세스별로 남은 날짜 계산
    for i in range(len(progresses)):
        left_days.append(math.ceil((100 - progresses[i])/speeds[i]))
    
    # 남은 날짜들을 서로 다음 프로세스와 비교해서 같이 배포할수 있는지 없는지를 판단
    for idx, day in enumerate(left_days):
        if idx == 0:
            now_left_day = left_days[idx]
        # 처음 프로세스가 아니라면 이전 프로세스와 같이 배포할수 있는지 판단
        else:
            # 다음프로세스가 더 오래 걸린다면 배포 횟수 확정
            if now_left_day < left_days[idx]:
                answer.append(deploy_count)
                now_left_day = left_days[idx]
                deploy_count = 1
            # 다음 프로세스 종료 일시가 더 빠르거나 같으면 같이 배포해야 하므로 배포 횟수 추가
            else:
                deploy_count += 1

    # 남은 날짜의 마지막 인덱스 배포판단 여부를 추가한다.
    answer.append(deploy_count)
    return answer
```

