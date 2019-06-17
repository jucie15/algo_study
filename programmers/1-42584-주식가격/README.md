### 해설
데이터셋이 10만개이고 최악의 경우 `prices`가 [1,2,3....100000]까지 갈 경우 `n^2`으로 안되지만 해당 문제의 경우 값이 10000까지라 `n^2`이 안나온다.
하여 `큐`를 이용해 리스트의 앞에서부터 값이 떨이지는 구간까지 계산 후 해당 값을 `큐`에서 `pop()`하고 다음 값부터 계산하는 형식으로 푸는걸 의도 한듯하다.
(Level 2 이기에)

시간복잡도: `O(n^2)`

공간복잡도: `O(n)`

```Python
    from collections import deque
    def solution(prices):
        answer = []
        sec = 0
        now = 0
        prices = deque(prices)

        while len(prices) > 1:
            sec = 0
            now = prices.popleft()

            for price in prices:
                if now > price:
                    sec = sec + 1
                    break
                else:
                    sec = sec + 1

            answer.append(sec)

        answer.append(0)

        return answer
```
