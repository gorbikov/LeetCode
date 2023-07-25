class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        def mountain_value(arr: list[int]) -> int:
            if len(arr) == 1:
                return arr[0]
            division_position = len(arr) // 2
            # Пик.
            if arr[division_position] > arr[division_position - 1] and arr[division_position] > arr[
                division_position + 1]:
                return arr[division_position]
            # Подъем.
            if arr[division_position - 1] <= arr[division_position] <= arr[division_position + 1]:
                return mountain_value([-float("inf")] + arr[division_position:])
            # Спуск.
            if arr[division_position - 1] >= arr[division_position] >= arr[division_position + 1]:
                return mountain_value(arr[:division_position] + [-float("inf")])

        return arr.index(mountain_value(arr))


s = Solution()
print("Example 1: ")
print(s.peakIndexInMountainArray([0, 1, 0]))  # 1
print("Example 2: ")
print(s.peakIndexInMountainArray([0, 2, 1, 0]))  # 1
print("Example 3: ")
print(s.peakIndexInMountainArray([0, 10, 5, 2]))  # 1
