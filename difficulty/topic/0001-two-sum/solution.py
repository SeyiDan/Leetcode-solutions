class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        summ = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in summ:
                return [summ[diff], i] 
            summ[nums[i]] = i
        return []

            
           
