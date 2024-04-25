class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count={}#Dictionary to store the character count

       #Count the character occurence
        for char in s:
            if char in char_count:
                char_count[char]+=1
            else:
                char_count[char]=1
        
        #Find the unique number
        for i,char in enumerate(s):
            if char_count[char]==1:
                return i
        return -1
