class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        substrings = {}

        def calculate_for_substring(s: str):
            return sum([ord(i) for i in s])

        def all_substrings(s1, s2, cur_substring):
            if not s1 or not s2:
                if cur_substring not in substrings:
                    substrings[calculate_for_substring(cur_substring)] = cur_substring
                cur_substring = ""
            for cur_pos_in_s1, cur_symbol_in_s1 in enumerate(s1):
                if cur_symbol_in_s1 not in s2:
                    if cur_substring not in substrings:
                        substrings[calculate_for_substring(cur_substring)] = cur_substring
                    continue
                else:
                    for cur_pos_in_s2, cur_symbol_in_s2 in enumerate(s2):
                        if cur_symbol_in_s2 == cur_symbol_in_s1:
                            new_cur_substring = cur_substring + cur_symbol_in_s1
                            all_substrings(s1[cur_pos_in_s1 + 1:], s2[cur_pos_in_s2 + 1:], new_cur_substring)

        all_substrings(s1, s2, "")
        max_substring = substrings.get(max(substrings.keys()))

        return calculate_for_substring(s1 + s2) - calculate_for_substring(max_substring) * 2

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        matrix = [[0 for i in range(len(s1)+2)] for j in range(len(s2) + 2)]
        for i in range(len(s1)):
            matrix[0][i + 2] = ord(s1[i])
        for j in range(len(s2)):
            matrix[j+2][0] = ord(s2[j])
        for i in range(len(s1)):
            for j in range(len(s2)):
                if s1[i] == s2[j]:
                    matrix[j+2][i+2] = matrix[j+1][i+1] + ord(s1[i])
                else:
                    matrix[j + 2][i + 2] = max(matrix[j + 1][i + 2], matrix[j + 2][i + 1])
        return sum([ord(i) for i in s1 + s2]) - 2 * matrix[-1][-1]



s = Solution()
print("Example 1: ")
print(s.minimumDeleteSum("sea", "eat"))  # 231
print("Example 2: ")
print(s.minimumDeleteSum("delete", "leet"))  # 403
print("Example 3: ")
print(s.minimumDeleteSum("sjfqkfxqoditw", "fxymelgo"))  # 1638
print("Example 4: ")
print(s.minimumDeleteSum("vwojt", "saqhgdrarwntji"))  # 1613
