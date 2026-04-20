class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = nums1 + nums2
        res.sort()
        n = len(res)
        if n%2 == 0:
            a = int((n/2)-1)
            b = int((n/2))
            temp = (res[a] + res[b])/2
        
        else:
            c = int(n/2)
            temp = res[c]
             
        return temp
        