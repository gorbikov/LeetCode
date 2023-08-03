class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        num_to_alphabet = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        k_start = len(digits)
        result = set()

        def recursion(digits, dict, curr, k, i):
            if k == 1:
                abc = dict[digits[i]]
                for symb in abc:
                    curr = curr + symb
                    result.add(curr)
                    curr = curr[:-1]
            else:
                curr = curr[:k_start - k]
                abc = dict[digits[i]]
                for symb in abc:
                    curr = curr + symb
                    recursion(digits, dict, curr, k - 1, i + 1)
                    curr = curr[:-1]

        if k_start == 0:
            return []
        recursion(digits, num_to_alphabet, "", k_start, 0)
        return result


s = Solution()
print("Example 1: ")
print(s.letterCombinations("23"))  # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print("Example 2: ")
print(s.letterCombinations(""))  # []
print("Example 3: ")
print(s.letterCombinations("2"))  # ["a","b","c"]
