from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        path_length = len(tickets)
        graph = defaultdict(list[str])
        for ticket in tickets:
            graph[ticket[0]].append(ticket[1])

        # Проверка на пустой массив.
        if path_length == 0:
            return []

        paths = []

        def find_path(prev_path, paths, graph, remaining_length):
            if remaining_length == 0:
                paths.append(prev_path.copy())
            else:
                current_node = prev_path[-1]
                current_next_nodes = graph[current_node]
                for next_node in current_next_nodes.copy():
                    prev_path.append(next_node)
                    remaining_length -= 1
                    graph[current_node].remove(next_node)
                    find_path(prev_path, paths, graph, remaining_length)
                    remaining_length += 1
                    graph[current_node].append(next_node)
                    prev_path.pop()

        find_path(["JFK"], paths, graph, path_length)

        paths_str = {}
        if len(paths) == 1:
            return paths[0]
        else:
            for pos, path in enumerate(paths):
                path_str = ""
                for el in path:
                    path_str += el
                paths_str[pos] = path_str

        paths_str_alphabet = dict(sorted(paths_str.items(), key=lambda x: x[1]))
        return paths[next(iter(paths_str_alphabet))]


s = Solution()
print("Example 1:", s.findItinerary(
    [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))  # ["JFK","MUC","LHR","SFO","SJC"]
print("Example 2:", s.findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"],
                                     ["ATL", "SFO"]]))  # ["JFK","ATL","JFK","SFO","ATL","SFO"]
print("Example 3:", s.findItinerary(
    [["AXA", "EZE"], ["EZE", "AUA"], ["ADL", "JFK"], ["ADL", "TIA"], ["AUA", "AXA"], ["EZE", "TIA"], ["EZE", "TIA"],
     ["AXA", "EZE"], ["EZE", "ADL"], ["ANU", "EZE"], ["TIA", "EZE"], ["JFK", "ADL"], ["AUA", "JFK"], ["JFK", "EZE"],
     ["EZE", "ANU"], ["ADL", "AUA"], ["ANU", "AXA"], ["AXA", "ADL"], ["AUA", "JFK"], ["EZE", "ADL"], ["ANU", "TIA"],
     ["AUA", "JFK"], ["TIA", "JFK"], ["EZE", "AUA"], ["AXA", "EZE"], ["AUA", "ANU"], ["ADL", "AXA"], ["EZE", "ADL"],
     ["AUA", "ANU"], ["AXA", "EZE"], ["TIA", "AUA"], ["AXA", "EZE"], ["AUA", "SYD"], ["ADL", "JFK"], ["EZE", "AUA"],
     ["ADL", "ANU"], ["AUA", "TIA"], ["ADL", "EZE"], ["TIA", "JFK"], ["AXA", "ANU"], ["JFK", "AXA"], ["JFK", "ADL"],
     ["ADL", "EZE"], ["AXA", "TIA"], ["JFK", "AUA"], ["ADL", "EZE"], ["JFK", "ADL"], ["ADL", "AXA"], ["TIA", "AUA"],
     ["AXA", "JFK"], ["ADL", "AUA"], ["TIA", "JFK"], ["JFK", "ADL"], ["JFK", "ADL"], ["ANU", "AXA"], ["TIA", "AXA"],
     ["EZE", "JFK"], ["EZE", "AXA"], ["ADL", "TIA"], ["JFK", "AUA"], ["TIA", "EZE"], ["EZE", "ADL"], ["JFK", "ANU"],
     ["TIA", "AUA"], ["EZE", "ADL"], ["ADL", "JFK"], ["ANU", "AXA"], ["AUA", "AXA"], ["ANU", "EZE"], ["ADL", "AXA"],
     ["ANU", "AXA"], ["TIA", "ADL"], ["JFK", "ADL"], ["JFK", "TIA"], ["AUA", "ADL"], ["AUA", "TIA"], ["TIA", "JFK"],
     ["EZE", "JFK"], ["AUA", "ADL"], ["ADL", "AUA"], ["EZE", "ANU"], ["ADL", "ANU"], ["AUA", "AXA"], ["AXA", "TIA"],
     ["AXA", "TIA"], ["ADL", "AXA"], ["EZE", "AXA"], ["AXA", "JFK"], ["JFK", "AUA"], ["ANU", "ADL"], ["AXA", "TIA"],
     ["ANU", "AUA"], ["JFK", "EZE"], ["AXA", "ADL"], ["TIA", "EZE"], ["JFK", "AXA"], ["AXA", "ADL"], ["EZE", "AUA"],
     ["AXA", "ANU"], ["ADL", "EZE"], ["AUA", "EZE"]]))  # ["JFK","ATL","JFK","SFO","ATL","SFO"]
