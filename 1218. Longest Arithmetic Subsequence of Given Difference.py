from collections import defaultdict
from heapq import heappop, heappush


class Solution:
    def longestSubsequence(self, arr: list[int], difference: int) -> int:
        def create_graph(arr, difference):
            graph = defaultdict(list)
            for curr_node, curr_val in enumerate(arr):
                for next_node, next_val in enumerate(arr):
                    if next_node <= curr_node:
                        continue
                    else:
                        if curr_val + difference == next_val:
                            graph[curr_node].append(next_node)
            return graph

        def find_head_nodes(graph):
            nodes = []
            for node in graph:
                write = True
                for next_node in graph:
                    if next_node >= node:
                        pass
                    if node in graph[next_node]:
                        write = False
                        break
                if write:
                    nodes.append(node)
            return nodes

        def find_longest_path_length(graph, node):
            min_heap = [(-1, node)]
            visited = set()
            result = 0

            while min_heap:
                length, node = heappop(min_heap)
                visited.add(node)
                for neighbor_node in graph[node]:
                    if neighbor_node not in visited:
                        heappush(min_heap, (length - 1, neighbor_node))
                        if result > length - 1:
                            result = length - 1
            return -result

        graph = create_graph(arr, difference)
        nodes = find_head_nodes(graph)
        if not graph:
            return 1
        else:
            result = 1
            for node in nodes:
                current_result = find_longest_path_length(graph, node)
                if current_result > result:
                    result = current_result
            return result


class SolutionDP:
    def longestSubsequence(self, arr: list[int], difference: int) -> int:
        sequences = defaultdict(list)
        for curr_pos, curr_val in enumerate(arr):
            for next_pos, next_val in enumerate(arr):
                if next_pos <= curr_pos:
                    pass
                else:
                    if curr_val + difference == next_val:
                        pair = [curr_val, next_val]
                        start_pos_of_pair = curr_pos
                        end_pos_of_pair = next_pos
                        if not sequences:
                            sequences[end_pos_of_pair] = [pair]
                        else:
                            for end_in_seq in list(sequences.keys()):
                                if end_in_seq == start_pos_of_pair:
                                    for num, seq_with_curr_end in enumerate(sequences[end_in_seq]):
                                        sequences[end_in_seq][num] = sequences[end_in_seq][num] + [pair[1]]
                                    sequences[end_pos_of_pair] = sequences[end_in_seq]
                                    del sequences[end_in_seq]
                                else:
                                    # TODO Что-то тут не так.
                                    sequences[end_pos_of_pair] = sequences[end_pos_of_pair] + [pair]
        print(sequences)
        if not sequences:
            return 1
        else:
            result = 1
            for end in sequences:
                for seq in sequences[end]:
                    if len(seq) > result:
                        result = len(seq)
            return result


s = SolutionDP()
print("Example 1: ")
print(s.longestSubsequence([1, 2, 3, 4], 1))  # 4
print("Example 2: ")
print(s.longestSubsequence([1, 3, 5, 7], 1))  # 1
print("Example 3: ")
print(s.longestSubsequence([1, 5, 7, 8, 5, 3, 4, 2, 1], -2))  # 4
print("Example 4: ")
print(s.longestSubsequence([1, 2, 3, 4, 8, 9, 10, 11, 12, 13], 1))  # 6
print("Example 5: ")
print(s.longestSubsequence([7, -2, 8, 10, 6, 18, 9, -8, -5, 18, 13, -6, -17, -1, -6, -9, 9, 9], 1))  # 3
