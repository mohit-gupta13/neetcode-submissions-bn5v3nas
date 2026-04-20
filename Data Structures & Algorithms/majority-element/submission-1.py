class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)

        res = maxcnt = 0

        for num in nums:
            count[num] += 1
            if maxcnt < count[num]:
                maxcnt = count[num]
                res = num
        return res