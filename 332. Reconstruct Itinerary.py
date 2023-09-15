from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        path_length = len(tickets)
        graph = defaultdict(list[str])
        for ticket in sorted(tickets):
            graph[ticket[0]].append(ticket[1])

        # Проверка на пустой массив.
        if path_length == 0:
            return []

        result = []

        def find_path(prev_path, result, graph, remaining_length):
            if remaining_length == 0:
                result.append(prev_path)
            else:
                if len(result) == 0:
                    current_node = prev_path[-1]
                    current_next_nodes = graph[current_node]
                    for next_node in current_next_nodes.copy():
                        if len(result) == 0:
                            prev_path.append(next_node)
                            remaining_length -= 1
                            graph[current_node].remove(next_node)
                            find_path(prev_path, result, graph, remaining_length)
                            if len(result) == 0:
                                remaining_length += 1
                                graph[current_node].append(next_node)
                                prev_path.pop()

        find_path(["JFK"], result, graph, path_length)
        return result[0]


s = Solution()
print("Example 1:", s.findItinerary(
    [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))  # ["JFK","MUC","LHR","SFO","SJC"]
print("Example 2:", s.findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"],
                                     ["ATL", "SFO"]]))  # ["JFK","ATL","JFK","SFO","ATL","SFO"]
print("Example 3:", s.findItinerary([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]))  # ["JFK","NRT","JFK","KUL"]
