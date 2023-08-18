from collections import defaultdict


class Solution:
    def maximalNetworkRank(self, n: int, roads: list[list[int]]) -> int:
        graph = defaultdict(list[int])
        # Чтобы потом легче было находить биггест сайз - ищем его во время заполнения.
        biggest_size = 0
        for el in roads:
            if el[0] in graph:
                if el[1] not in graph[el[0]]:
                    graph[el[0]] = graph[el[0]] + [el[1]]
                    biggest_size = max(biggest_size, len(graph[el[0]]))
            else:
                graph[el[0]] = [el[1]]
                if graph[el[1]] is None:
                    graph[el[1]] = [el[0]]
                elif el[0] not in graph[el[1]]:
                    graph[el[1]] = graph[el[1]] + [el[0]]
                    biggest_size = max(biggest_size, len(graph[el[1]]))
            if el[1] in graph:
                if el[0] not in graph[el[1]]:
                    graph[el[1]] = graph[el[1]] + [el[0]]
                    biggest_size = max(biggest_size, len(graph[el[1]]))
            else:
                graph[el[1]] = [el[0]]
                if graph[el[0]] is None:
                    graph[el[0]] = [el[1]]
                elif el[1] not in graph[el[0]]:
                    graph[el[0]] = graph[el[0]] + [el[1]]
                    biggest_size = max(biggest_size, len(graph[el[0]]))

        max_rank = 0

        # Если связей нет вообще.
        if biggest_size == 0:
            return 0

        for first_node in graph:
            if len(graph[first_node]) == biggest_size:
                for second_node in graph:
                    if first_node == second_node:
                        continue
                    elif second_node in graph[first_node]:
                        max_rank = max(max_rank, biggest_size + len(graph[second_node]) - 1)
                    else:
                        max_rank = max(max_rank, biggest_size + len(graph[second_node]))

        return max_rank

s = Solution()
print("Example 1: ")
print(s.maximalNetworkRank(4, [[0, 1], [0, 3], [1, 2], [1, 3]]))  # 4
print("Example 2: ")
print(s.maximalNetworkRank(5, [[0, 1], [0, 3], [1, 2], [1, 3], [2, 3], [2, 4]]))  # 5
print("Example 3: ")
print(s.maximalNetworkRank(8, [[0, 1], [1, 2], [2, 3], [2, 4], [5, 6], [5, 7]]))  # 5
print("Example 3: ")
print(s.maximalNetworkRank(8, []))  # 0
