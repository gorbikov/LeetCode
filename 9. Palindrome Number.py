class Solution:
    def isPalindrome(self, x: int) -> bool:
        return x >= 0 and x == int(str(x)[::-1])


s = Solution()
print("Example 1: ")
print(s.isPalindrome(121))
print("Example 2: ")
print(s.isPalindrome(-121))
print("Example 3: ")
print(s.isPalindrome(10))
