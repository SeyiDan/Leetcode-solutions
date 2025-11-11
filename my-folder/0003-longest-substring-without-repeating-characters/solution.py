class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set() #to track unique characters
        left = 0 #first pointer
        max_length = 0 #to calculate the max_length
        
        #using the second pointer to scan for duplicate
        for right in range(len(s)):
            #if duplicate found, keep reducing left until duplicate is eliminated
            while s[right] in charset:
                charset.remove(s[left])
                left+=1
            charset.add(s[right]) #keep adding if right is not in charset
            max_length = max(max_length, right - left +1)
        return max_length











        # charSet = set()
        # left = 0
        # res = 0

        # for right in range(len(s)):
        #     while s[right] in charSet:
        #         charSet.remove(s[left])
        #         left +=1
        #     charSet.add(s[right])
        #     res = max(res, right - left + 1 )
        # return res

        

