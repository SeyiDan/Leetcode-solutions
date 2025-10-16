# Contains Duplicate
# Difficulty: Easy
# Language: Python3
# Runtime: 11 ms
# Submission Date: 2025-05-06

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
           
        
