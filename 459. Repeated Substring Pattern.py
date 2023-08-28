class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        sub_length = len(s) // 2
        while sub_length > 0:
            if len(s) % sub_length == 0:
                sub = s[0: sub_length]
                sub_num = len(s) // sub_length
                ok = True
                for i in range(sub_num):
                    if sub != s[i * sub_length: (i + 1) * sub_length]:
                        ok = False
                if ok:
                    return True
            sub_length -= 1
        return False


s = Solution()
print("Example 1:")
print(s.repeatedSubstringPattern("abab"))  # True
print("Example 2:")
print(s.repeatedSubstringPattern("aba"))  # False
print("Example 3:")
print(s.repeatedSubstringPattern("abcabcabcabc"))  # True
