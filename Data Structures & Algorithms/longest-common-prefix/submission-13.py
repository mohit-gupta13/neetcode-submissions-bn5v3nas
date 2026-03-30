class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minlen=min(len(s) for s in strs)
        for i in range(minlen):
            for s in strs:
                if s[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0][:minlen]