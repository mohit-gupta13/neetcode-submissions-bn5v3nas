class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        n = len(heights)
        for i in range(n):
            h = heights[i]
            l = r = i
            max_area = max(max_area,h)
            while l >= 0 and heights[l] >= h:
                l -= 1
            while r < n and heights[r] >= h:
                r += 1
            area = h * (r - l - 1)
            max_area = max(max_area,area)

        return max_area
