class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start: int, end: int) -> float:
        # Проверка на наличие пути.
        is_connected = False


        #Расчёт по вариантам путей, если накопленная вероятность превышает текущий минимум - расчёт прекращается.








        return is_connected










s = Solution()
print("Example 1: ")
print(s.maxProbability(3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.2], 0, 2))
print("Example 2: ")
print(s.maxProbability(3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.3], 0, 2))
print("Example 3: ")
print(s.maxProbability(3, [[0,1]], [0.5], 0, 2))