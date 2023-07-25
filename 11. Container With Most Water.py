class Solution:
    def maxArea(self, height: list[int]) -> int:
        result = 0
        for pos1, val1 in enumerate(height):
            for pos2, val2 in enumerate(height[pos1:]):
                result = max(result, min(val1, val2) * abs(pos2))
        return result


class Solution2:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        result = min(height[left], height[right]) * (right - left)
        while left < right:
            curr_left = height[left]
            curr_right = height[right]
            if curr_left > curr_right:
                while curr_right >= height[right] and left < right:
                    right -= 1
                result = max(result, min(height[left], height[right]) * (right - left))
            else:
                while curr_left >= height[left] and left < right:
                    left += 1
                result = max(result, min(height[left], height[right]) * (right - left))

        return result


s = Solution2()
print("Example 1: ")
print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
print("Example 2: ")
print(s.maxArea([1, 1]))  # 1
