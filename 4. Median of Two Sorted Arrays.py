from statistics import median


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        return median(nums1+nums2)




s = Solution()
print("Example 1: ")
print(s.findMedianSortedArrays([1, 3], [2]))
print("Example 2: ")
print(s.findMedianSortedArrays([1, 2], [3, 4]))
