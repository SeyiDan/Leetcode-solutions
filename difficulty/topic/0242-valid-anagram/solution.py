class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        
        letter = {}
        for i in s:
            if i in letter:
                letter[i]+=1
            else:
                letter[i]=1

        for i in t:
            if i not in letter:
                return False
            letter[i]-=1

            if letter[i]<0:
                return False
            
        for count in letter.values():
            if count!=0:
                return False
        return True
            

