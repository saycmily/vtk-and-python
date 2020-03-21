def longestPalindrome(self, s: str) -> int:
    from collections import Counter
    c = Counter(s)
    ans = 0
    flag = False
    for value in c.values():
        if value == 1:
            flag = True
            continue
        if value % 2 == 1:
            ans += value - 1
            flag = True
        else:
            ans += value
    return ans + 1 if flag else ans
