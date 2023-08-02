class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = set()

        def reccursion(nums, k, curr, ises):
            i = 0
            if k == 1:
                while i < len(nums):
                    if i in ises:
                        i += 1
                    else:
                        curr.append(nums[i])
                        result.add(tuple(curr))
                        curr = curr[:-1]
                        i += 1
            else:
                while i < len(nums):
                    if i in ises:
                        i += 1
                    else:
                        curr = curr[:len(nums) - k]
                        ises = ises[:len(nums) - k]
                        curr.append(nums[i])
                        ises.append(i)
                        reccursion(nums, k - 1, curr, ises)
                        i += 1

        reccursion(nums, len(nums), [], [])
        return list([list(i) for i in result])


s = Solution()
print("Example 1: ")
print(s.permute([1, 2, 3]))  # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
print("Example 2: ")
print(s.permute([0, 1]))  # [[0,1],[1,0]]
print("Example 3: ")
print(s.permute([1]))  # [[1]]
