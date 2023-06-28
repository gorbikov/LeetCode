class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_counter = 0
        for pos, char in enumerate(s):
            unique_chars = {char}
            counter = 1
            if counter > max_counter:
                max_counter = counter
            for next_char in s[pos+1:]:
                if next_char not in unique_chars:
                    counter += 1
                    if counter > max_counter:
                        max_counter = counter
                    unique_chars.add(next_char)
                else:
                    break
        return max_counter

s = Solution()
print("Example 1: ")
print(s.lengthOfLongestSubstring("abcabcbb"))
print("Example 2: ")
print(s.lengthOfLongestSubstring("bbbbb"))
print("Example 3: ")
print(s.lengthOfLongestSubstring("pwwkew"))
print("Example 4: ")
print(s.lengthOfLongestSubstring("dvdf"))
