class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = defaultdict(int)
        n = len(nums)
        resu = []

        for num in nums:
            res[num] += 1
            if res[num] > n//3:
                resu.append(num)

        return list(set(resu))     