class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        """
        19. 06. 26
        풀이: target 값에서 nums[i] 값을 뺀다
        ex) target=9, nums[0]=2 면 뺀 값은 7 -> 7이라는 값의 유무를 조사한 뒤 있으면, 인덱스를 추출해서 반환
        But, nums = [3, 2, 4], target = 6 인 경우에 [0, 0]이라는 경우가 발생할 수 있어 두 번째 if 조건 추가

        """

        length = len(nums)
        idx = []
        
        for i in range(length):
            if (target-nums[i]) in nums:
                if i != nums.index(target-nums[i]):
                    idx.append(i)
                    idx.append(nums.index(target-nums[i]))
                    #idx.sort()
                    return idx