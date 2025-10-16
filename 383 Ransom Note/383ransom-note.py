class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter_note = {}

        for ch in magazine:
            if ch in letter_note:
                letter_note[ch]+=1
            else:
                letter_note[ch]=1

        for ch in ransomNote:
            if ch in letter_note and letter_note[ch]>0:
                letter_note[ch]-=1 
            else:   
                return False
        return True
        
        



            
             

#Time Complexity:
#Space Complexity:
        