class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_str = ''
        n = min(len(word1),len(word2))

        l=0
        while l < n:
            new_str += word1[l]
            new_str += word2[l]
            l += 1
        
        new_str += word2[l:] 
        new_str += word1[l:] 

        return new_str
