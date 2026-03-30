class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        b = 0
        e = len(s)-1
        for i in range(len(s)//2):
            s[b],s[e] = s[e],s[b]
            b += 1
            e -= 1
