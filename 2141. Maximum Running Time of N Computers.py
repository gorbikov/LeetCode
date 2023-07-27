from heapq import heapify, heappop, heappush


class Solution1:
    def maxRunTime(self, n: int, batteries: list[int]) -> int:
        batteries = [-i for i in batteries]
        heapify(batteries)
        computers = [-heappop(batteries) for i in range(n)]
        heapify(computers)
        curr_time = 0
        while computers[0] != 0:
            computers = [computers[i] - 1 for i in range(n)]
            curr_time += 1
            while len(batteries) != 0 and computers[0] == 0:
                heappop(computers)
                heappush(computers, -heappop(batteries))
            while len(batteries) != 0 and computers[0] < -batteries[0]:
                heappush(batteries, -heappop(computers))
                heappush(computers, -heappop(batteries))

        return curr_time


class Solution2:
    def maxRunTime(self, n: int, batteries: list[int]) -> int:
        """
        Через равномерное распределение оставшихся батареек по 1 единицу мощности за раз.

        :param n:
        :param batteries:
        :return:
        """
        computers = [batteries.pop(batteries.index(max(batteries))) for i in range(n)]
        additional_battery_hours = sum(batteries)
        while additional_battery_hours > 0:
            computers[computers.index(min(computers))] += 1
            additional_battery_hours -= 1
        return min(computers)


class Solution3:
    def maxRunTime(self, n: int, batteries: list[int]) -> int:
        """
        Через равномерное распределение оставшихся батареек по 1 единицу мощности за раз.
        Плюс компьютеры и перераспределение будем делать с учётом сортировки.

        :param n:
        :param batteries:
        :return:
        """
        computers = [batteries.pop(batteries.index(max(batteries))) for i in range(n)]
        additional_battery_hours = sum(batteries)
        while additional_battery_hours > 0:
            last_index = len(computers) - 1
            k = last_index
            while computers[k] == computers[last_index] and k >= 0:
                k -= 1
            computers[k+1] += 1
            additional_battery_hours -= 1
        return min(computers)


class Solution4:
    def maxRunTime(self, n: int, batteries: list[int]) -> int:
        """
        Самое хитрое решение с binary search.

        :param n:
        :param batteries:
        :return:
        """
        # Минимальное и максимальное количество часов.
        min_hours = 1
        max_hours = sum(batteries) // n


        while min_hours < max_hours:
            # Среднее между ними для проверки
            mid_point = max_hours - (max_hours - min_hours) // 2
            # Проверка для mid_point.
            if sum(min(battery, mid_point) for battery in batteries) >= mid_point * n:
                min_hours = mid_point
            else:
                max_hours = mid_point - 1
        return min_hours

s = Solution4()
print("Example 1: ")
print(s.maxRunTime(2, [3, 3, 3]))  # 4
print("Example 2: ")
print(s.maxRunTime(2, [1, 1, 1, 1]))  # 2
print("Example 3: ")
print(s.maxRunTime(3, [10, 10, 3, 5]))  # 8
print("Example 4: ")
print(s.maxRunTime(4, [8, 1, 4, 8]))  # 1
print("Example 5: ")
print(s.maxRunTime(2, [31, 87, 85, 44, 47, 25]))  # 159
