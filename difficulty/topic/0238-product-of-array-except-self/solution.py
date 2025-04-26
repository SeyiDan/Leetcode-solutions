class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # n = len(nums)
        # # Initialize the result array with 1s
        # result = [1] * n
        
        # # First pass: Calculate products of all elements to the left
        # left_product = 1
        # for i in range(n):
        #     result[i] = left_product
        #     left_product *= nums[i]
        
        # # Second pass: Calculate products of all elements to the right
        # # and multiply with the left products
        # right_product = 1
        # for i in range(n-1, -1, -1):
        #     result[i] *= right_product
        #     right_product *= nums[i]
        
        # return result
        l_mult = 1
        r_mult = 1
        n = len(nums)
        l_arr = [0] * n
        r_arr = [0] * n
        
        for i in range(n): 
            j = -i -1
            l_arr[i] = l_mult
            r_arr[j] = r_mult
            l_mult *= nums[i]
            r_mult *= nums[j]

        return [l*r for l, r in zip(l_arr, r_arr)]  
