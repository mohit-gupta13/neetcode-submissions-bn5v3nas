class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        temp = []
        res = []


        for r in range(k):
            temp.append(nums[r])

            if (r - l + 1) == k:
                res.append(max(temp))
                temp.pop(0)
                l += 1

        return res
        