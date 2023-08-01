class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p =

        if s == "" and len(p) == 2 and p[1] == "*":
            return True
        if s == "" and len(p) > 2 and p[1] == "*":
            return self.isMatch(s, p[2:])
        elif s == "" and p == "":
            return True
        elif s == "" and p != "":
            return False
        elif s != "" and p == "":
            return False
        elif len(p) >= 2 and p[1] == "*":
            if s[0] == p[0] or p[0] == ".":
                return self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
            else:
                return self.isMatch(s, p[2:])
        match = p[0] in {s[0], "."}
        return match and self.isMatch(s[1:], p[1:])


s = Solution()
print("Example 1: ")
print(s.isMatch("aa", "a"))  # False
print("Example 2: ")
print(s.isMatch("aa", "a*"))  # True
print("Example 3: ")
print(s.isMatch("ab", ".*"))  # True
print("Example 4: ")
print(s.isMatch("sdfgkljsdhfglkjhsdfg", "sdfgklj...fglk.hsdf."))  # True
print("Example 5: ")
print(s.isMatch("sdfgkljsdhfglkjhsdf", "sdfgklj...fglk.hsdf."))  # False
print("Example 6: ")
print(s.isMatch("sdfgkljsdhfglkjhsdfg", "sdfgklj...fglk.hs"))  # False
print("Example 7: ")
print(s.isMatch("aaa", "a*a"))  # True
print("Example 8: ")
print(s.isMatch("aaa", "ab*a*c*a"))  # True
print("Example 8: ")
print(s.isMatch("aabcbcbcaccbcaabc", ".*a*aa*.*b*.c*.*a*"))  # True
print("Example 9: ")
print(s.isMatch("aaaaaaaaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*"))  # True
