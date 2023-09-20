class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        nums_len = len(nums)
        current_sum = x
        stop_left = False
        stop_right = False
        result = 0
        if nums_len == 0:
            return -1
        for i in range(nums_len):
            left = nums[0]
            right = nums[-1]
            left_delta = current_sum - left
            right_delta = current_sum - right
            if left_delta < 0:
                stop_left = True
            if right_delta < 0:
                stop_right = True
            if stop_left and stop_right:
                return -1
            if stop_left:
                current_sum -= right
                nums = nums[:-1]
            elif stop_right:
                current_sum -= left
                nums = nums[1:]
            else:
                if left_delta <= right_delta:
                    current_sum -= left
                    nums = nums[1:]
                else:
                    current_sum -= right
                    nums = nums[:-1]
            result += 1
            if current_sum == 0:
                return result
        if current_sum != 0:
            return -1


class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        nums_len = len(nums)
        stop = False
        deltas = [[-1 for _ in range(nums_len + 1)] for _ in range(nums_len + 1)]
        result = float("inf")
        for count_left, row_deltas in enumerate(deltas):
            stop = False
            for count_right, delta in enumerate(row_deltas):
                if stop:
                    pass
                left_nums = nums[:count_left]
                right_nums = nums[nums_len-count_right:]
                delta = x - sum(left_nums) - sum(right_nums)
                if delta == 0:
                    deltas[count_left][count_right] = delta
                    result = min(result, count_left + count_right)
                if delta > 0:
                    deltas[count_left][count_right] = delta
                else:
                    stop = True
        if result > nums_len:
            return -1
        else:
            return result

s = Solution()
print("Example 1:", s.minOperations([1, 1, 4, 2, 3], 5))  # 2
print("Example 2:", s.minOperations([5, 6, 7, 8, 9], 4))  # -1
print("Example 3:", s.minOperations([3, 2, 20, 1, 1, 3], 10))  # 5
print("Example 4:", s.minOperations([1, 1], 3))  # -1
print("Example 5:", s.minOperations(
    [5207, 5594, 477, 6938, 8010, 7606, 2356, 6349, 3970, 751, 5997, 6114, 9903, 3859, 6900, 7722, 2378, 1996, 8902,
     228, 4461, 90, 7321, 7893, 4879, 9987, 1146, 8177, 1073, 7254, 5088, 402, 4266, 6443, 3084, 1403, 5357, 2565, 3470,
     3639, 9468, 8932, 3119, 5839, 8008, 2712, 2735, 825, 4236, 3703, 2711, 530, 9630, 1521, 2174, 5027, 4833, 3483,
     445, 8300, 3194, 8784, 279, 3097, 1491, 9864, 4992, 6164, 2043, 5364, 9192, 9649, 9944, 7230, 7224, 585, 3722,
     5628, 4833, 8379, 3967, 5649, 2554, 5828, 4331, 3547, 7847, 5433, 3394, 4968, 9983, 3540, 9224, 6216, 9665, 8070,
     31, 3555, 4198, 2626, 9553, 9724, 4503, 1951, 9980, 3975, 6025, 8928, 2952, 911, 3674, 6620, 3745, 6548, 4985,
     5206, 5777, 1908, 6029, 2322, 2626, 2188, 5639], 565610))  # 113
