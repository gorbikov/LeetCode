class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start: int, end: int) -> float:
        current_max_succ_prob = 0

        def path_finder(n: int, edges: list[list[int]], succProb: list[float], start: int, end: int):
            for el in edges:
                if current_point in el:
                    current_point_index =
                    if !(el[!el.index(current_point)] in passed_points):

            def path_finder(n: int, edges: list[list[int]], succProb: list[float], start: int, end: int)




        return current_max_succ_prob



s = Solution()
print("Example 1: ")
print(s.maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2))
print("Example 2: ")
print(s.maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.3], 0, 2))
print("Example 3: ")
print(s.maxProbability(3, [[0, 1]], [0.5], 0, 2))
