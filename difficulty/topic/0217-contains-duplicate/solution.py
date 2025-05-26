class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numss=set()

        for i in nums:
            if i in numss:
                return True
            numss.add(i)

        return False
