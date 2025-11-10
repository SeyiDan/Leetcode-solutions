class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
    
        for i, num in enumerate(nums):
            diff  = target - num 
            if diff in seen:
                return [seen[diff],i]
            else:
                seen[num]=i
        return None










        
        # seen = {}

        # for i, num in enumerate(nums):
        #     diff = target - num
        #     if diff in seen:
        #         return[seen[diff],i]
        #     seen[num]=i
        # return None












        # seen = {}

        # for i, num in enumerate(nums):
        #     diff = target - num
        #     if diff in seen:
        #         return [seen[diff],i]
        #     seen[num]=i
        # return None





































        # summ ={}

        # for i,num in enumerate(nums):
        #     diff = target - num
        #     if diff in summ:
        #         return [summ[diff],i]
        #     summ[num]=i

































        # summ = {}

        # for i,num in enumerate(nums):
        #     diff = target - num
        #     if diff in summ:
        #         return [summ[diff],i]
        #     summ[num]=i











        # summ = {}

        # for i, num in enumerate(nums):
        #     diff = target - num
        #     if diff in summ:
        #         return [summ[diff], i]
        #     summ[num] = i

            
           
