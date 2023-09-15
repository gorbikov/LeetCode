from collections import defaultdict


class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        if len(points) == 0:
            return 0
        graph = defaultdict(list[list[int]])
        for num1, point1 in enumerate(points):
            for num2, point2 in enumerate(points):
                if num1 == num2:
                    pass
                else:
                    graph[num1].append([num2, abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])])

        result = []
        visited_nodes = [0]

        def find_nex_node(graph, visited_nodes):
            if len(visited_nodes) < len(points):
                min_distance = float('inf')
                min_distance_node = -1
                for visited_node in visited_nodes:
                    for node, distance in graph[visited_node]:
                        if node in visited_nodes:
                            pass
                        else:
                            if distance < min_distance:
                                min_distance = distance
                                min_distance_node = node
                result.append(min_distance)
                visited_nodes.append(min_distance_node)
                find_nex_node(graph, visited_nodes)

        find_nex_node(graph, visited_nodes)
        return sum(result)


s = Solution()
print("Example 1:", s.minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))  # 20
print("Example 2:", s.minCostConnectPoints([[3, 12], [-2, 5], [-4, 1]]))  # 18
