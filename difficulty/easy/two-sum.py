# Two Sum
# Difficulty: Easy
# Language: Python3
# Runtime: 54 ms
# Submission Date: 2023-10-07

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} #val:index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[n] = i
        return

