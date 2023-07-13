class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if "" in strs:
            return ""
        else:
            result = ""
            counter = 0
            while counter < len(strs[0]):
                current_first_word_symbol = strs[0][counter:counter + 1]
                for word in strs:
                    current_symbol = word[counter:counter + 1]
                    if current_first_word_symbol != current_symbol:
                        return result
                counter += 1
                result = result + current_symbol
            return result


s = Solution()
print("Example 1: ")
print(s.longestCommonPrefix(["flower", "flow", "flight"]))
print("Example 2: ")
print(s.longestCommonPrefix(["dog", "racecar", "car"]))
print("Example 3: ")
print(s.longestCommonPrefix(["a"]))
