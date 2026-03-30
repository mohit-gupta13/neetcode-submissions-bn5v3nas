class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        for num in nums:
            cnt = 0
            for i in range(n):
                if nums[i] == num:
                    cnt += 1
            if cnt >= n/2:
                return num         

        