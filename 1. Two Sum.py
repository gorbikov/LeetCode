class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        set_of_numbers: dict = {}
        for position1, value1 in enumerate(nums):
            target_minus_first_value = target - value1
            if target_minus_first_value in set_of_numbers:
                return [set_of_numbers[target_minus_first_value], position1]
            else:
                set_of_numbers[nums[position1]] = position1


s = Solution()
print("Example 1: ")
print(s.twoSum([2, 7, 11, 15], 9))
print("Example 2: ")
print(s.twoSum([3, 2, 4], 6))
print("Example 3: ")
print(s.twoSum([3, 3], 6))
print("Example 4: ")
print(s.twoSum([-1, -2, -3, -4, -5], -8))
