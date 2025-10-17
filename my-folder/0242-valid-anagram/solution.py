class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Critical: anagrams must have identical lengths
        if len(s)!= len(t):
            return False
        letter_count = {}

        for ch in s:
            if ch in letter_count:
                letter_count[ch]+=1
            else:
                letter_count[ch]=1

        for ch in t:
            if ch in letter_count and letter_count[ch]>0:
                letter_count[ch]-=1
            else:
                return False
        return True


















































        # if len(s) != len(t):
        #     return False
        
        # letter_count = {}
        
        # for ch in s:
        #     if ch in letter_count:
        #         letter_count[ch] += 1
        #     else:
        #         letter_count[ch] = 1
        
        # for ch in t:
        #     if ch in letter_count and letter_count[ch] > 0:
        #         letter_count[ch] -= 1
        #     else:
        #         return False
        
        # return True

