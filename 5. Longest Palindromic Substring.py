class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        reversed_s = s[::-1]
        for start, letter in enumerate(s):
            end = -1
            while True:
                end = reversed_s.find(letter, end + 1)
                if end == -1:
                    break
                if reversed_s[end: len(s) - start] == s[start: len(s) - end]:
                    if len(s) - end - start > len(result):
                        result = s[start: len(s) - end]

        return result


s = Solution()
print("Example 1: ")
print(s.longestPalindrome("babad"))
print("Example 2: ")
print(s.longestPalindrome("cbbd"))
print("Example 2: ")
print(s.longestPalindrome("a"))
