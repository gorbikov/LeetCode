class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Убирает ситуацию типа a*aaaa, превращает её просто в a*.
        def delete_repeatings_after_star(p: str) -> str:
            current_find_index = 0
            while p.find("*", current_find_index) != -1:
                next_star_index = p.find("*", current_find_index)
                if next_star_index + 1 < len(p):
                    if p[next_star_index - 1] == p[next_star_index + 1]:
                        p = p[:next_star_index + 1] + p[next_star_index + 2:]
                    else:
                        current_find_index = next_star_index + 1
                else:
                    break
            return p

        # Преобразовали p, чтобы не было повторений после звёздочки.
        p = delete_repeatings_after_star(p)

        pos_in_s = 0

        for pos_in_p in range(len(p)):
            # Создаём окно.
            window = p[pos_in_p: pos_in_p + 2]

            # Если .*.
            if window[0] == "." and window[1] == "*":
                return True
            # Одна буква.
            if window[0].isalpha() and len(window) == 1:
                if window[0] == s[pos_in_s] and pos_in_s == len(s) - 1:
                    return True
                else:
                    return False
            # Одна точка.
            if window[0] == "." and len(window) == 1:
                if pos_in_s == len(s) - 1:
                    return True
                else:
                    return False
            # Одна звёздочка в конце.
            if window[0] == "*" and len(window) == 1:
                if pos_in_s == len(s) - 1:
                    return True
                else:
                    return False
            # Буква и не * за ней.
            if window[0].isalpha() and window[1] != "*":
                if window[0] == s[pos_in_s]:
                    if pos_in_s == len(s) - 1:
                        return False
                    else:
                        pos_in_s += 1
                        continue
                else:
                    return False
            # Точка и не * за ней.
            if window[0] == "." and window[1] != "*":
                if pos_in_s == len(s) - 1:
                    return False
                else:
                    pos_in_s += 1
                    continue
            # Пара со звёздочкой в конце.
            if window[0].isalpha() and window[1] == "*":
                while pos_in_s < len(s) and window[0] == s[pos_in_s]:
                    if pos_in_s == len(s) - 1:
                        return True
                    else:
                        pos_in_s += 1
                        continue
                else:
                    if pos_in_s == len(s) - 1:

                    pos_in_s = min(pos_in_s, len(s) - 1)
                    continue
            # Пара со звёздочкой в начале.
            if window[0] == "*" and window[1].isalpha():
                if pos_in_s ==
                    continue


        return True


s = Solution()
# print("Example 1: ")
# print(s.isMatch("aa", "a"))  # False
print("Example 2: ")
print(s.isMatch("aa", "a*"))  # True
print("Example 3: ")
print(s.isMatch("ab", ".*"))  # True
print("Example 4: ")
print(s.isMatch("aab", "c*a*b"))  # True
print("Example 5: ")
print(s.isMatch("aab", "....c*ccca*aaaa.."))  # True
