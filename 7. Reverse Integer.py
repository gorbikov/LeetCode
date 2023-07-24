from struct import pack


class Solution:
    def reverse(self, x: int) -> int:
        f = lambda res: int(str(x)[::-1]) if x >= 0 else int('-' + str(-x)[::-1])
        try:
            pack("i", f(x))
        except:
            return 0
        return f(x)


s = Solution()
print("Example 1: ")
print(s.reverse(123))  # 321
print("Example 2: ")
print(s.reverse(-123))  # -321
print("Example 3: ")
print(s.reverse(120))  # 21
