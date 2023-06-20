class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = list(s)
        result = 0
        dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4,
                "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        for count, value in enumerate(letters):
            if count != len(letters) - 1 and dict[value] < dict[letters[count + 1]]:
                result -= dict[value]
            else:
                result += dict[value]
        return result


s = Solution()
print("Example 1: ")
print(s.romanToInt("III"))
print("Example 2: ")
print(s.romanToInt("LVIII"))
print("Example 3: ")
print(s.romanToInt("MCMXCIV"))
