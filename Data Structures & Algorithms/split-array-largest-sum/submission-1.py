class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def cansplit(largest):
            subarray = 1
            cursum = 0
            for num in nums:
                cursum += num
                if cursum > largest:
                    subarray += 1
                    if subarray > k :
                        return False
                    cursum = num
            return True

        l, r = max(nums),sum(nums)
        res = r

        while l <= r:
            mid = (l+r)//2

            if cansplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res