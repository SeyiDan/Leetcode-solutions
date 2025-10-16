# Jewels and Stones
# Difficulty: Easy
# Language: Python3
# Runtime: 3 ms
# Submission Date: 2025-10-16

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)
        count = 0

        for i in stones:
            if i in jewel_set:
                count+=1
        return count


































        # jewel_set= set(jewels)
        # count=0

        # for stone in stones:
        #     if stone in jewel_set:
        #         count+=1
        # return count
        
