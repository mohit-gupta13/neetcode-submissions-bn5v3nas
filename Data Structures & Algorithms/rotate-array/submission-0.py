class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = [0]*len(nums)
        n = len(nums)
        for i in range(len(nums)):
            res[(i + k) % n] = nums[i]

        nums[:] = res

        