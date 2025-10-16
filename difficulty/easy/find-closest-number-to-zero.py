# Find Closest Number to Zero
# Difficulty: Easy
# Language: Python3
# Runtime: 5 ms
# Submission Date: 2025-10-06

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]

        for x in nums:
            if abs(x)<abs(closest) or (abs(x)==abs(closest) and x>closest):
                closest = x

        return closest















        # closest = nums[0]

        # for x in nums:
        #     if abs(x)<abs(closest):
        #         closest = x
        #     if abs(x)==abs(closest) and x>closest:
        #         closest = x
        # return closest
        
