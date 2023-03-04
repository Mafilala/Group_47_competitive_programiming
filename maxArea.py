class Solution:
    def maxArea(self, height):
        max_area = float(-inf)
        left = 0
        right = len(height) - 1
        while left < right:
            area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, area)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return max_area

        
