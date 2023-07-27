class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums = sorted(nums)
        l = 0
        c = l + 1
        r = len(nums) - 1

        def check_and_add(left_pointer, center_pointer, right_pointer):
            if nums[left_pointer] + nums[center_pointer] + nums[right_pointer] > 0:
                return 1
            elif nums[left_pointer] + nums[center_pointer] + nums[right_pointer] < 0:
                return -1
            else:
                threeSum = [nums[left_pointer], nums[center_pointer], nums[right_pointer]]
                if threeSum not in result:
                    result.append(threeSum)
                return 0

        while l < c < r:
            while c < r:
                if check_and_add(l, c, r) == 1:
                    r -= 1
                else:
                    c += 1
            l += 1
            c = l + 1
            r = len(nums) - 1

        return result

class Solution2:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums = sorted(nums)
        l = 0
        c = l + 1
        r = len(nums) - 1

        while l < c < r:
            while c < r:
                if nums[l] + nums[c] + nums[r] > 0:
                    r -= 1
                elif nums[l] + nums[c] + nums[r] < 0:
                    c += 1
                else:
                    if [nums[l], nums[c], nums[r]] not in result:
                        result.append([nums[l], nums[c], nums[r]])
                    c += 1
            l += 1
            c = l + 1
            r = len(nums) - 1

        return result

s = Solution2()
print("Example 1: ")
print(s.threeSum([-1, 0, 1, 2, -1, -4]))  # [[-1,-1,2],[-1,0,1]]
print("Example 2: ")
print(s.threeSum([0, 1, 1]))  # []
print("Example 3: ")
print(s.threeSum([0, 0, 0]))  # [[0,0,0]]
print("Example 4: ")
print(s.threeSum([-1,0,1,2,-1,-4]))  # [[-1,-1,2],[-1,0,1]]
