class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        min_delta = float("inf")
        nearest_sum = float("inf")
        sign = None
        nums.sort()
        for pos1, num1 in enumerate(nums):
            for pos2, num2 in enumerate(nums):
                for pos3, num3 in enumerate(nums):
                    if pos1 < pos2 < pos3:
                        delta = num1 + num2 + num3 - target
                        if delta == 0:
                            return num1 + num2 + num3
                        if delta > 0:
                            current_sign = 1
                        else:
                            current_sign = -1
                        if sign is None:
                            sign = current_sign
                        if abs(delta) < min_delta:
                            min_delta = abs(delta)
                            nearest_sum = num1 + num2 + num3
                        if sign != current_sign:
                            break

        return nearest_sum


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        num_length = len(nums)
        min_delta = float("inf")
        nearest_sum = float("inf")
        nums.sort()
        for i in range(num_length - 2):
            j = i + 1
            k = num_length - 1
            while j < k:
                sum_of_three = nums[i] + nums[j] + nums[k]
                delta = sum_of_three - target
                if delta == 0:
                    return sum_of_three
                elif abs(delta) < min_delta:
                    min_delta = abs(delta)
                    nearest_sum = sum_of_three
                if delta > 0:
                    k -= 1
                else:
                    j += 1

        return nearest_sum


s = Solution()
print("Example 1:", s.threeSumClosest([-1, 2, 1, -4], 1))  # 2
print("Example 2:", s.threeSumClosest([0, 0, 0], 1))  # 0
print("Example 3:", s.threeSumClosest([0, 3, 97, 102, 200], 300))  # 300
print("Example 4:", s.threeSumClosest([4, 0, 5, -5, 3, 3, 0, -4, -5], -2))  # -2
