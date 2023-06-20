class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_dict = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10,
                      "IX": 9, "V": 5, "IV": 4, "I": 1}
        result = []

        for key in roman_dict.keys():
            value = roman_dict[key]
            while num >= value:
                result.append(key)
                num -= roman_dict[key]

        return "".join(result)


s = Solution()
print("Example 1: ")
print(s.intToRoman(3))
print("Example 2: ")
print(s.intToRoman(58))
print("Example 3: ")
print(s.intToRoman(1994))
