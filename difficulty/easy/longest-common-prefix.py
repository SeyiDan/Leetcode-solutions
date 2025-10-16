# Longest Common Prefix
# Difficulty: Easy
# Language: Python3
# Runtime: 1 ms
# Submission Date: 2025-10-12

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for i in range(len(strs[0])):
            for s in strs:
                if i ==len(s) or s[i]!=strs[0][i]:
                    return res
            res+=strs[0][i]
        return res





















        # res = ""

        # for i in range(len(strs[0])):
        #     for s in strs:
        #         if i == len(s) or s[i]!=strs[0][i]:
        #             return res
        #     res+=strs[0][i]
        # return res
            


        
