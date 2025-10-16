# Two Sum
# Difficulty: Easy
# Language: Python3
# Runtime: 0 ms
# Submission Date: 2025-05-09

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        summ = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in summ:
                return [summ[diff], i]
            summ[nums[i]]=i
        return summ
            
           
