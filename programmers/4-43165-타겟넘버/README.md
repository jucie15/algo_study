### 해설

    탐색문제로 재귀를 통해 모든 경우의 수 체크

    n = 2 <= numbers < 20

    m = 1 <= target <= 1000

    시간복잡도: `O(2^n)`

    공간복잡도: `O(n+m)`

```python
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
```
