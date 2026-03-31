class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        
        while l <= r:
            mid = (l+r)//2
            daystaken = 1
            capacity = mid

            for w in weights:
                if w <= capacity:
                   capacity -= w
                else:
                    daystaken += 1
                    capacity = mid
                    capacity -= w

            if daystaken > days:
                l = mid + 1
            else:
                r = mid - 1


        return l