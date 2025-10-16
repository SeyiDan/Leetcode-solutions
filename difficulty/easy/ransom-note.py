# Ransom Note
# Difficulty: Easy
# Language: Python3
# Runtime: 26 ms
# Submission Date: 2025-05-08

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter_count={}


        for ch in magazine:
            if ch in letter_count:
                letter_count[ch]+=1
            else:
                letter_count[ch]=1
        
        for ch in ransomNote:
            if ch in letter_count and letter_count[ch]>0:
                letter_count[ch]-=1
            else:
                return False
        return True

#Time Complexity:
#Space Complexity:
        
