# Contains Duplicate
# Difficulty: Easy
# Language: Python3
# Runtime: 13 ms
# Submission Date: 2025-10-16

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        







        numss=set()

        for i in nums:
            if i in numss:
                return True
            numss.add(i)

        return False
