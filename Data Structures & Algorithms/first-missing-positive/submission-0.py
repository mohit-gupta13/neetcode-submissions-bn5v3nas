class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 1
        while True:
            if i not in nums:
                return i
            else:
                i += 1
                