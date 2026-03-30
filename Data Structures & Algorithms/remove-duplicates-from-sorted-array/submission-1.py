class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = sorted(set(nums))
        nums[:len(seen)] = seen
        return len(seen)
        