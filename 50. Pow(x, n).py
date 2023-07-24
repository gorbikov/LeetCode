import functools


class Solution1:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if x == 1:
            return x
        if x == -1:
            return lambda res: 1 if n // 2 == 0 else -1
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1 / x

        def rec_func(x, n):
            if n == 1:
                return x
            x = x * rec_func(x, n - 1)
            return x

        return rec_func(x, n)


class Solution2:
    @functools.cache
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n < 0:
            n = -n
            x = 1 / x
        return self.myPow(x, n // 2) * self.myPow(x, n // 2) * self.myPow(x, n % 2)


s = Solution2()
print("Example 1: ")
print(s.myPow(2.00000, 10))  # 1024.00000
print("Example 2: ")
print(s.myPow(2.10000, 3))  # 9.26100
print("Example 3: ")
print(s.myPow(2.00000, -2))  # 0.25000
print("Example 4: ")
print(s.myPow(0.00001, 2147483647))  # 0.25000
