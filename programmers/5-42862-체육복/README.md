### 해설

    `reverse`와 `lost`에서 중복된 값을 먼저 제거해 준 후 빌려줄 수 있는 사람이 있는 지 체크 후 빌려준다.(`_lost.remove`)
    `answer` = `n - len(_lost)`

n = 전체학생 수

m = lost의 길이

j = reserve의 길이

시간복잡도: `O(m*j)`

공간복잡도: `O(m+j)`

```python
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]

    for r in _reserve:
        if r - 1 in _lost:
            _lost.remove(r - 1)
        elif r + 1 in _lost:
            _lost.remove(r + 1)

    return n - len(_lost)
```
