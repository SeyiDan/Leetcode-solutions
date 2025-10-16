# Find Closest Number to Zero
# Difficulty: Easy
# Language: Python3
# Runtime: 6 ms
# Submission Date: 2025-04-21

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]

        for x in nums:
            if abs(x) < abs(closest):
                closest = x
            elif abs(x)==abs(closest) and x > closest:
                closest = x

        return closest

       
