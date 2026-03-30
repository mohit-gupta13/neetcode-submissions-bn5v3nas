class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x

        while left <= right:
            mid = (left + right)//2
            res = mid * mid

            if res==x:
                return mid
            elif res < x:
                left = mid + 1
            else:
                right = mid - 1
        return right
