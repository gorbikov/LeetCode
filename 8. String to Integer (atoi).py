class Solution:
    def myAtoi(self, s: str) -> int:
        is_positive = True
        sign_passed = False
        leading_spaces = True
        leading_zeros = True
        result = ""
        boundaries = [-2 ** 31, 2 ** 31 - 1]
        max_len = len(str(boundaries[1]))
        for symb in s:
            if symb == " " and leading_spaces:
                continue
            if symb == "-" and not sign_passed:
                is_positive = False
                sign_passed = True
                leading_spaces = False
                continue
            if symb == "+" and not sign_passed:
                sign_passed = True
                leading_spaces = False
                continue
            if symb == "0" and leading_zeros:
                sign_passed = True
                leading_spaces = False
                continue

            if symb.isdigit():
                sign_passed = True
                leading_spaces = False
                leading_zeros = False
                result += symb
                if len(result) > max_len:
                    break
            else:
                if sign_passed:
                    break
                else:
                    result = "0"
                    break

        if result == "":
            return 0
        else:
            result = int(result)

        if is_positive:
            return min(result, boundaries[1])
        else:
            return max(-result, boundaries[0])


s = Solution()
print("Example 1: ")
print(s.myAtoi("42"))  # 42
print("Example 2: ")
print(s.myAtoi("   -42"))  # -42
print("Example 3: ")
print(s.myAtoi("4193 with words"))  # 4193
print("Example 4: ")
print(s.myAtoi("words and 987"))  # 0
print("Example 5: ")
print(s.myAtoi("+-12"))  # 0
print("Example 6: ")
print(s.myAtoi("21474836460"))  # 2147483647
print("Example 7: ")
print(s.myAtoi("  0000000000012345678"))  # 12345678
print("Example 8: ")
print(s.myAtoi("00000-42a1234"))  # 0
print("Example 9: ")
print(s.myAtoi("0  123"))  # 0
