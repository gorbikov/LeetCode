import itertools
from collections import defaultdict
from heapq import heappop, heappush


class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start: int, end: int) -> float:

        def find_all_paths(n, start, end):
            """Строит все возможные ребра, через которые можно пройти между start и end."""
            all_points = list(range(n))
            all_points.remove(start)
            all_points.remove(end)
            all_points = all_points + ['empty'] * len(all_points)
            all_permutations = itertools.permutations(all_points, r=int(len(all_points) / 2))
            all_paths = []
            for i in all_permutations:
                i = list(i)
                while 'empty' in i: i.remove('empty')
                all_paths.append(tuple([start] + i + [end]))

            return (list(set(all_paths)))

        def delete_impossible_paths(all_paths, edges):
            """Оставляет только возможные пути с учётом edges."""
            possible_paths = []
            for current_path in all_paths:
                possible = True
                for i in range(len(current_path) - 1):
                    window = [current_path[i], current_path[i + 1]]
                    reversed_window = [current_path[i + 1], current_path[i]]
                    if not (window in edges) and not (reversed_window in edges):
                        possible = False
                        break
                if possible:
                    possible_paths.append(current_path)

            return possible_paths

        def calculate_max_prob(possible_paths, edges, succProb):
            max_prob = 0
            for current_path in possible_paths:
                current_prob = 1
                for i in range(len(current_path) - 1):
                    window = [current_path[i], current_path[i + 1]]
                    reversed_window = [current_path[i + 1], current_path[i]]
                    if window in edges:
                        index = edges.index(window)
                        current_prob *= succProb[index]
                    else:
                        index = edges.index(reversed_window)
                        current_prob *= succProb[index]
                if current_prob > max_prob:
                    max_prob = current_prob
            return max_prob

        all_paths = find_all_paths(n, start, end)
        possible_paths = delete_impossible_paths(all_paths, edges)
        if not possible_paths:
            return 0
        else:
            return calculate_max_prob(possible_paths, edges, succProb)


class SolutionDijkstra:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start: int, end: int) -> float:
        probabilities = [-float("inf")] * n
        is_traveled = [False] * n
        numbers = list(range(n))
        probabilities[start] = 1
        while True:
            current_point_probability, current_point_index = max(
                (x, z) for x, y, z in zip(probabilities, is_traveled, numbers) if y is False)
            neighbor_point_indexes = []
            edges_to_neighbor_from_current_point = []
            for edge in edges:
                if current_point_index in edge:
                    if edge[0] == current_point_index and is_traveled[edge[1]] is False:
                        neighbor_point_indexes.append(edge[1])
                        edges_to_neighbor_from_current_point.append(edge)
                    elif edge[1] == current_point_index and is_traveled[edge[0]] is False:
                        neighbor_point_indexes.append(edge[0])
                        edges_to_neighbor_from_current_point.append(edge)
            for neighbor_point_index, edge_to_neighbor in zip(neighbor_point_indexes,
                                                              edges_to_neighbor_from_current_point):
                current_edge_probability = succProb[edges.index(edge_to_neighbor)]
                if current_point_probability * current_edge_probability > probabilities[neighbor_point_index]:
                    probabilities[neighbor_point_index] = current_point_probability * current_edge_probability
            is_traveled[current_point_index] = True
            if current_point_index == end:
                break
        if probabilities[end] == -float("inf"):
            return 0
        else:
            return probabilities[end]


class SolutionDijkstraHeapq:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start: int, end: int) -> float:
        # Создаём граф.
        graph = defaultdict(list)
        # Наполняем граф.
        # Т.к. мы планируем использовать min_heap как max_heap - здесь и далее вероятности отрицательны.
        # Точки без связей вообще нре попадут в этот граф.
        for e, p in zip(edges, succProb):
            graph[e[0]].append([e[1], -p])
            graph[e[1]].append([e[0], -p])

        # Создаём кучу.
        min_heap = [(-1, start)]

        # Создаём сет для перечисления посещенных точек.
        visited = set()

        # Если куча опустела переходим к выводу нулевого значения.
        while min_heap:
            # Берем данные текущего нода и удаляем его из кучи (он больше не понадобится).
            p, node = heappop(min_heap)
            # Метим удаленную ноду как посещенную.
            visited.add(node)
            # Если мы дошли до финиша - выводим полученный результат.
            if node == end:
                return -p
            # Перебираем соседние ноды.
            for neighbor_node, pn in graph[node]:
                if neighbor_node not in visited:
                    # Проверку на то, что записанное значение будет меньше старого можно не делать,
                    # т.к. оба варианта останутся в куче и через heappop будет выбран для результата наименьший.
                    heappush(min_heap, (-p * pn, neighbor_node))
        return 0


s = SolutionDijkstraHeapq()
print("Example 1: ")
print(s.maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2))
print("Example 2: ")
print(s.maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.3], 0, 2))
print("Example 3: ")
print(s.maxProbability(3, [[0, 1]], [0.5], 0, 2))
print("Example 4: ")
print(s.maxProbability(5, [[0, 1], [0, 2], [1, 3], [3, 4]], [0.5, 0.3, 0.2, 0.1], 0, 2))
print("Example 5: ")
print(s.maxProbability(4, [[0, 1], [1, 2], [2, 3]], [0.5, 0.5, 0.5], 0, 3))
print("Example 6: ")
print(s.maxProbability(10, [[0, 3], [1, 7], [1, 2], [0, 9]], [0.31, 0.9, 0.86, 0.36], 2, 3))
