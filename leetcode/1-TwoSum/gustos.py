# 코드1이 가장 빠른 이유가 궁금


# 코드 1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, num in enumerate(nums):
            for idx2 in range(idx + 1, len(nums)):
                if num + nums[idx2] == target:
                    return [idx, idx2]


# 코드 2
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, num in enumerate(nums):
            for idx2, num2 in enumerate(nums[idx+1:], idx + 1):
                if num + num2 == target:
                    return [idx, idx2]


# 코드 3
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        len_nums = len(nums)
        for idx in range(len_nums):
            for idx2 in range(idx + 1, len_nums):
                if nums[idx] + nums[idx2] == target:
                    return [idx, idx2]
