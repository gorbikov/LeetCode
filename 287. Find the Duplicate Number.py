class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        passed_numbers = set()
        n = len(nums)
        for i in range(n):
            if len(passed_numbers) == 0:
                passed_numbers.add(nums[i])
            else:
                if nums[i] in passed_numbers:
                    return nums[i]
                else:
                    passed_numbers.add(nums[i])


s = Solution()
print("Example 1:", s.findDuplicate([1, 3, 4, 2, 2]))  # 2
print("Example 2:", s.findDuplicate([3, 1, 3, 4, 2]))  # 3
