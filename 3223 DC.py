from collections import Counter
class Solution:
    def minimumLength(self, s: str) -> int:
        # given string s, select i st
        # 1 char at index j st j < i and s[j] = s[i] and 1 char at index k st k > i and s[k] = s[i]
        # delete char at index j and k
        """
        pattern:
        1 -> 1
        2 -> 2
        3 -> f(1) -> 1
        4 -> f(2) -> 2
        5 -> f(3) -> 1
        6 -> f(4) -> 2
        ...

        alternating 1, 2
        """

        f = Counter(s)
        res = 0
        for char in f.keys():
            res += (2 - (f[char] % 2))
        return res