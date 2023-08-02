class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = set()
        start_k = k
        numbers = [i+1 for i in range(n)]
        def reccursion (numbers, k, curr, i):
            if k == 1:
                while i < len(numbers) - k + 1:
                    curr.append(numbers[i])
                    result.add(tuple(curr))
                    curr = curr[:-1]
                    i += 1

            while i < len(numbers) - k + 1:
                curr = curr[:start_k - k]
                curr.append(numbers[i])
                reccursion(numbers, k-1, curr, i+1)
                i += 1

        reccursion(numbers, k, [], 0)
        return list([list(i) for i in result])

s = Solution()
print("Example 1: ")
print(s.combine(4, 2))  # [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
print("Example 2: ")
print(s.combine(1, 1))  # [[1]]
print("Example 3: ")
print(s.combine(4, 3))  # [[1,2,3],[1,2,4],[1,3,4],[2,3,4]]
print("Example 4: ")
print(s.combine(3, 3))  # [[1,2,3],[1,2,4],[1,3,4],[2,3,4]]
