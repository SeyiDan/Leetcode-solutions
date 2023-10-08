class Solution:
     def twoSum(self, nums: List[int], target: int) -> List[int]:
         #create a hashmap that stores the elements and it's indices
         prevMap =  {}

         #loop through the hashmap 
         for i,n in enumerate(nums):
             diff = target - n
             if diff in prevMap:
                 return [prevMap[diff], i]
             prevMap[n] = i
         return




























    #    #create a hashmap that stores the elements and its indices
    #    prevMap ={}

    #    #iterate through the array to find diff(element needed to add up to the target)
    #    for i, n in enumerate(nums):
    #        #check if the element is in the hashmap
    #        diff = target - n

    #        #return a pair of element and indicesif it is
    #        if diff in prevMap:
    #         return[prevMap[diff], i]

    #        #if not, update hashmap with prev element/index
    #        prevMap[n]=i
    #    return



       

