### 해설
    순열을 이용하여 모든 경우의 수를 도출한 후 정수로 변환('011'등의 숫자가 가능하기에)하고
    중복('101'등의 숫자가 가능)을 제거한 후 해당 순열에서 소수 갯수 계산

n = 1 <= numbers <= 7

시간복잡도: 몇인가...더 최적화 가능한가??
공간복잡도: O(순열의 총 갯수)

```python
import itertools

def solution(numbers):
    per_list = set()
    answer = 0
    for i in range(1, len(numbers) + 1):
        per_list |= set(map(int, map(''.join, itertools.permutations(numbers, i))))

    for p in per_list:
        if is_prime(p):
            answer += 1

    return answer

def is_prime(number):
    number = int(number)
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0 or number == 1 or number == 0:
            return False

    return True
```
