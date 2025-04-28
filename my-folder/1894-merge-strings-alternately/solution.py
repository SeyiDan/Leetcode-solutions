class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Initialize pointers and result list
        i, j = 0, 0
        merged = []

        # Merge strings alternately
        while i < len(word1) and j < len(word2):
            merged.append(word1[i])
            merged.append(word2[j])
            i += 1
            j += 1

        # Append remaining characters (if any)
        if i < len(word1):
            merged.append(word1[i:])
        if j < len(word2):
            merged.append(word2[j:])

        # Join list into a string and return
        return ''.join(merged)

