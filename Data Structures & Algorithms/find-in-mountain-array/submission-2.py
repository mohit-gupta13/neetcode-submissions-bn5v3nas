class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        peak = self.findpeakindex(mountainArr)
        l,r = 0,peak

        while l <= r:
            mid = (l+r)//2

            num = mountainArr.get(mid)

            if num == target:
                return mid
            elif num < target:
                l = mid + 1
            else:
                r = mid - 1

        l,r = peak,mountainArr.length() - 1

        while l <= r:
            mid = (l+r)//2

            num = mountainArr.get(mid)

            if num == target:
                return mid
            elif num < target:
                r = mid - 1
            else:
                l = mid + 1

        return -1



    def findpeakindex(self,mountainArr):
        l,r =0, mountainArr.length() - 1

        while l < r:

            mid = (l+r)//2

            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                l = mid + 1
            else:
                r = mid
        return r
