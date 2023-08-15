import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums = [-i for i in nums]
        heapq.heapify(nums)
        for i in range(k):
            result = heapq.heappop(nums)
        return -result


s = Solution()
print("Example 1: ")
print(s.findKthLargest([3, 2, 1, 5, 6, 4], 2))  # 5
print("Example 2: ")
print(s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # 4
