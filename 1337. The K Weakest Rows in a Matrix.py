class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        if len(mat) == 0:
            return []
        row_dict = {}
        result = []
        for num, mat_row in enumerate(mat):
            row_dict[num] = sum(mat_row)

        row_dict = dict(sorted(row_dict.items(), key=lambda x: x[1]))

        return list(row_dict.keys())[0:k]


s = Solution()
print("Example 1:", s.kWeakestRows([[1, 1, 0, 0, 0],
                                    [1, 1, 1, 1, 0],
                                    [1, 0, 0, 0, 0],
                                    [1, 1, 0, 0, 0],
                                    [1, 1, 1, 1, 1]], 3))  # [2,0,3]
print("Example 2:", s.kWeakestRows([[1, 0, 0, 0],
                                    [1, 1, 1, 1],
                                    [1, 0, 0, 0],
                                    [1, 0, 0, 0]], 2))  # [0,2]

print("Example 3:", s.kWeakestRows([], 0))  # []
