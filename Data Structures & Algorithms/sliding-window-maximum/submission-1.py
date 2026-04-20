class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        temp = []
        res = []


        for r in range(k):
            temp.append(nums[r])

        res.append(max(temp))

        for r in range(k,len(nums)):
            l += 1
            temp.pop(0)
            temp.append(nums[r])
            res.append(max(temp))
        return res
        