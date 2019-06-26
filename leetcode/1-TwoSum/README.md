### 해설


    target 값에서 리스트의 원소 값을 빼준 뒤, 그 값의 유무를 확인 후
    있으면 인덱스 값을 추출한다. 정답은 target에서 값을 뺀 원소의 인덱스 값과, 뺀 결과 값의 인덱스 값으로 이루어진 리스트이다.

시간복잡도: `O(nlogn)`

공간복잡도: `O(n)`



```python
class Solution(object):
    def twoSum(self, nums, target):

        length = len(nums)
        idx = []
        
        for i in range(length):
            if (target-nums[i]) in nums:
                if i != nums.index(target-nums[i]):
                    idx.append(i)
                    idx.append(nums.index(target-nums[i]))
                    return idx

```