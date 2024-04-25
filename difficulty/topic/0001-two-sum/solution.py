class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sto_re = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in sto_re:
                 return [sto_re[complement], i]
            sto_re[nums[i]]=i
        return sto_re

                

            
