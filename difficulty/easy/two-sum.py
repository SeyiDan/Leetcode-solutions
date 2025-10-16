# Two Sum
# Difficulty: Easy
# Language: Python3
# Runtime: 0 ms
# Submission Date: 2025-03-07

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        store = {} #Dictionary to store the numbers

        #find the two numbers
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in store:
                return[store[complement],i]
            store[nums[i]]=i
        return store
                


