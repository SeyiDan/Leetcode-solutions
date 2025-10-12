class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        i = 0
        
        while i < len(nums):
            start = nums[i]
            
            # Move forward while consecutive numbers continue
            while i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
                i += 1
            
            # Add range or single number
            if start != nums[i]:
                ans.append(f"{start}->{nums[i]}")
            else:
                ans.append(str(nums[i]))
            
            i += 1  # Move to next range
        
        return ans
