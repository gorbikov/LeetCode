from heapq import heapify, heappop, heappush


class Solution:
    def maxRunTime(self, n: int, batteries: list[int]) -> int:
        batteries = [-i for i in batteries]
        heapify(batteries)
        computers = [-heappop(batteries) for i in range(n)]
        heapify(computers)
        curr_time = 0
        while computers[0] != 0:
            computers = [computers[i] - 1 for i in range(n)]
            curr_time += 1
            while computers[0] == 0 and not batteries:
                heappop(computers)
                heappush(computers, -heappop(batteries))
            while computers[0] < -batteries[0]:
                heappush(batteries, -heappop(computers))
                heappush(computers, -heappop(batteries))

        return curr_time


s = Solution()
print("Example 1: ")
print(s.maxRunTime(2, [3, 3, 3]))  # 4
print("Example 2: ")
print(s.maxRunTime(2, [1, 1, 1, 1]))  # 2
print("Example 3: ")
print(s.maxRunTime(2, [3, 4, 5, 1]))  # 2
